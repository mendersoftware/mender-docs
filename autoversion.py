#!/usr/bin/python3
# Copyright 2018 Northern.tech AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import argparse
import os
import re
import subprocess

UPDATE = 1
CHECK = 2
MODE = UPDATE

INTEGRATION_REPO = None
VERSION = None

# Match version strings.
VERSION_MATCHER = r"(?:(?<![0-9]\.)(?<![0-9])[1-9][0-9]*\.[0-9]+\.[x0-9]+(?:b[0-9]+)?(?![0-9])(?!\.[0-9])|(?<![a-z])master(?![a-z]))"

VERSION_CACHE = {}

def get_version_of(repo):
    version = VERSION_CACHE.get(repo)
    if version is None:
        version = subprocess.check_output([os.path.join(INTEGRATION_REPO, "extra", "release_tool.py"),
                                           "--version-of", repo,
                                           "--in-integration-version", VERSION]
        ).strip().decode()
        VERSION_CACHE[repo] = version
    return version

def walk_tree():
    for dirpath, dirnames, filenames in os.walk("."):
        for file in filenames:
            if not file.endswith(".md") and not file.endswith(".markdown"):
                continue

            if (dirpath.endswith("Release-notes-changelog")
                or dirpath.endswith("Open-source-licenses")):
                # These files are exempt, since they are supposed to refer to
                # old versions.
                continue

            process_file(os.path.join(dirpath, file))

def process_file(file):
    if MODE == UPDATE:
        newname = "%s.new" % file
        new = open(newname, "w")
    else:
        new = None
    lineno = 0
    try:
        with open(file) as orig:
            tag_search = re.compile("^ *<!-- *AUTOVERSION *:")
            # When empty, signals that autoversioning is not active. When
            # filled, contains replacements to be made on the line.
            replacements = []
            in_code_block = False
            for line in orig.readlines():
                lineno += 1
                if not in_code_block and tag_search.match(line):
                    replacements = parse_autoversion_tag(line)
                    if MODE == UPDATE:
                        new.write(line)
                    continue
                if line.startswith("```"):
                    if in_code_block:
                        in_code_block = False
                        replacements = []
                    else:
                        in_code_block = True

                process_line(line, replacements, new)

                if not in_code_block and len(line.strip()) == 0:
                    # Outside code blocks we only keep replacement list for one
                    # paragraph, separated by empty line.
                    replacements = []
        if MODE == UPDATE:
            new.close()
            os.rename(newname, file)
    except Exception as exc:
        if MODE == UPDATE:
            new.close()
            os.remove(newname)

        # A little hacky: Extend the error message with the filename.
        args = exc.args
        if not args:
            arg0 = ''
        else:
            arg0 = args[0]
        arg0 = '%s:%d: %s' % (file, lineno, arg0)
        exc.args = (arg0, ) + args[1:]
        raise

def parse_autoversion_tag(tag):
    # Returns a structure like this:
    # [
    #     {
    #         "search": For example: "-b %" to match -b parameter with version.
    #         "repo": Git repository whose version should be substituted.
    #     },
    #     ...
    # ]

    # Match a string like:
    # <!--AUTOVERSION: "-b %"/integration "integration-%"/integration-->
    # and allow escaped double quotes in the match string (inside double quotes
    # in example).
    tag_match = re.match('^ *<!-- *AUTOVERSION *: *(.*)--> *$', tag)
    if not tag_match:
        raise Exception("Malformed AUTOVERSION tag:\n%s" % tag)
    end_of_whole_tag = tag_match.end(1)

    matcher = re.compile(r'"((?:[^"]|\\")*)"/([^/ ]+) *')
    last_end = -1
    parsed = []
    pos = tag_match.start(1)
    while True:
        match = matcher.match(tag, pos=pos, endpos=end_of_whole_tag)
        if not match:
            break
        pos = match.end()
        last_end = pos
        expr = match.group(1).replace('\\"', '"')
        repo = match.group(2)
        if "%" not in expr and repo != "complain":
            raise Exception("Search string \"%s\" doesn't contain at least one '%%' (only allowed in \"complain\" mode)" % search)
        parsed.append({"search": expr, "repo": repo})
    if last_end != end_of_whole_tag:
        raise Exception(("AUTOVERSION tag not parsed correctly:\n%s"
                         + "Example of valid tag:\n"
                         '<!--AUTOVERSION: "git clone -b %%"/integration "Mender client %%"/mender "docker version %%"/ignore-->')
                        % tag)
    return parsed

def process_line(line, replacements, fd):
    # Process a line using the given replacements, optionally writing to a file
    # if it is not None.

    # First run a pass over the line, where we remove all replacements, and then
    # check if there are any "version-looking" strings left, which there should
    # not be.
    all_removed = do_replacements(line, replacements, just_remove=True)
    match = re.search(VERSION_MATCHER, all_removed)
    if match:
        sep = "-------------------------------------------------------------------------------"
        raise Exception(('Found version-looking string "%s" in documentation line, not covered by any AUTOVERSION expression. '
                         + 'Original line:\n\n%s\n%s%s\n\n'
                         + 'AUTOVERSION expressions in effect:\n%s\n\n'
                         + 'Line after removing all AUTOVERSION matched sections:\n\n%s\n%s%s\n\n'
                         + 'See README-autoversion.markdown for more information.')
                        % (match.group(0), sep, line, sep,
                           "None" if len(replacements) == 0 else "\n".join(['"%s"/%s' % (repl['search'], repl['repo']) for repl in replacements]),
                           sep, all_removed, sep))

    # If we were not given a file, then we are just doing checking and are done.
    if fd is None:
        return

    # Now do the replacement and write that.
    all_replaced = do_replacements(line, replacements, just_remove=False)
    fd.write(all_replaced)

def do_replacements(line, replacements, just_remove):
    all_replaced = line
    for search, repo in [(repl["search"], repl["repo"]) for repl in replacements]:
        if len(search.strip()) <= 2:
            raise Exception("Search string needs to be longer/more specific than just '%s'" % search)
        escaped = re.escape(search)
        regex = escaped.replace("\%", VERSION_MATCHER)
        if not just_remove and repo == "complain":
            if re.search(regex, all_replaced):
                raise Exception("Requires manual fixing so it doesn't match \"complain\" expression:\n%s" % line)
            else:
                continue
        if just_remove:
            repl = search.replace("%", "")
        else:
            if repo == "ignore":
                continue
            version = get_version_of(repo)
            repl = search.replace("%", version)
        all_replaced = re.sub(regex, repl, all_replaced)
    return all_replaced

def main():
    global MODE
    global INTEGRATION_REPO
    global VERSION

    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true",
                        help="Check that there are no dangling version references")
    parser.add_argument("--update", action="store_true",
                        help="Update all version references")
    parser.add_argument("--integration-dir", metavar="DIR",
                        help="Location of integration repository")
    parser.add_argument("--version",
                        help="Mender version to update to")
    args = parser.parse_args()

    if args.update and args.check:
        raise Exception("--check and --update are mutually exclusive")
    elif args.update:
        if args.integration_dir is None or args.version is None:
            raise Exception("--update argument requires both --integration-dir and --version arguments")
        MODE = UPDATE
        INTEGRATION_REPO = args.integration_dir
        VERSION = args.version
    elif args.check:
        MODE = CHECK
    else:
        raise Exception("Either --check or --update must be given")

    walk_tree()

if __name__ == "__main__":
    main()
