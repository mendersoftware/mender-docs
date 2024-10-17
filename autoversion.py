#!/usr/bin/python3
# Copyright 2019 Northern.tech AS
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
import sys
import json
from urllib.request import urlopen

UPDATE = 1
CHECK = 2
MODE = UPDATE
IGNORE_COMPLAIN = False

INTEGRATION_REPO = None
INTEGRATION_VERSION = None

# Match version strings.
YOCTO_BRANCHES = r"(?:dora|daisy|dizzy|jethro|krogoth|morty|pyro|rocko|sumo|thud|warrior|zeus|dunfell|gatesgarth|kirkstone|langdale|mickledore|scarthgap)"
EXACT_VERSION_MATCH = r"(?<![0-9]\.)(?<![0-9])[1-9][0-9]*\.[0-9]+\.[x0-9]+(?:b[0-9]+)?(?:-build[0-9]+)?(?![0-9])(?!\.[0-9])"
VERSION_MATCHER = r"(?:%s|(?:mender-%s)|(?<![a-z])(?:%s|master)(?![a-z]))" % (
    EXACT_VERSION_MATCH,
    EXACT_VERSION_MATCH,
    YOCTO_BRANCHES,
)
MINOR_VERSIONS_MATCHER = r"(?:(?<!\.)\s*\d+\.\d+[, ]?(?!\.\d))+"

VERSION_CACHE = {}

ERRORS_FOUND = False

VERSIONS_URL = "https://docs.mender.io/releases/versions.json"
response = urlopen(VERSIONS_URL)
versions = json.loads(response.read())
RELEASED_VERSION_CACHE = versions or {}


def get_released_version_of(repo):
    minor_version = ""
    if INTEGRATION_VERSION:
        minor_version = INTEGRATION_VERSION[0 : INTEGRATION_VERSION.rfind(".")]
    if (
        not minor_version
        or not "releases" in RELEASED_VERSION_CACHE
        or not minor_version in RELEASED_VERSION_CACHE["releases"]
    ):
        return None
    info = next(
        (
            info
            for info in RELEASED_VERSION_CACHE["releases"][minor_version][
                INTEGRATION_VERSION
            ]["repos"]
            if info["name"] == repo
        ),
        {},
    )
    if "version" in info:
        return info["version"]


def get_version_of(repo):
    global VERSION_CACHE

    version = VERSION_CACHE.get(repo)
    if version is False:
        return None
    elif version is not None:
        return version
    elif INTEGRATION_REPO is not None and INTEGRATION_VERSION is not None:
        result = subprocess.run(
            [
                os.path.join(INTEGRATION_REPO, "extra", "release_tool.py"),
                "--version-of",
                repo,
                "--version-type",
                "git",
                "--in-integration-version",
                INTEGRATION_VERSION,
            ],
            capture_output=True,
        )
        if result.stderr or result.returncode == 1:
            VERSION_CACHE[repo] = False
            return None
        version = result.stdout.strip().decode()
        VERSION_CACHE[repo] = version
        return version
    else:
        released_version = None
        try:
            released_version = get_released_version_of(repo)
        except KeyError:
            print(
                f"Version not found in {VERSIONS_URL}. It may take time to reach it. Try running with --integration-dir instead, to get the information from there."
            )
        if released_version:
            VERSION_CACHE[repo] = released_version
            return released_version
        else:
            print('Not replacing "%s" instances, since it was not specified' % repo)
            VERSION_CACHE[repo] = False
            return None


def get_lts_versions():
    global VERSION_CACHE

    lts_versions = ", ".join(RELEASED_VERSION_CACHE["lts"])
    VERSION_CACHE["lts"] = lts_versions
    return lts_versions


def walk_tree():
    exclude_dirs = [
        "node_modules",  # Several readme.md with version strings
        "03.Open-source-licenses",  # References to old versions
    ]
    for dirpath, dirs, filenames in os.walk(".", topdown=True):
        dirs[:] = list(filter(lambda x: not x in exclude_dirs, dirs))
        for file in filenames:
            if not file.endswith(".md") and not file.endswith(".markdown"):
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

            first_line = True

            in_page_header = False
            page_header_lines = []

            for line in orig.readlines():
                lineno += 1

                # Deal with page header which may have a following tag instead
                # of a preceding tag.
                if first_line:
                    first_line = False
                    if line.strip() == "---":
                        in_page_header = True
                        page_header_lines.append(line)
                        continue
                if in_page_header:
                    page_header_lines.append(line)
                    if line.strip() == "---":
                        in_page_header = False
                    continue

                # Deal with code blocks.
                if not in_code_block and tag_search.match(line):
                    replacements = parse_autoversion_tag(line)
                    # Apply replacing/checking to page header blocks.
                    if len(page_header_lines) > 0:
                        for ph_line in page_header_lines:
                            process_line(ph_line, replacements, new)
                        page_header_lines = []
                    if MODE == UPDATE:
                        new.write(line)
                    continue
                if line.startswith("```"):
                    if in_code_block:
                        in_code_block = False
                        replacements = []
                    else:
                        in_code_block = True

                # Apply replacing/checking to page header blocks.
                if len(page_header_lines) > 0:
                    for ph_line in page_header_lines:
                        process_line(ph_line, replacements, new)
                    page_header_lines = []

                # Actual replacing/checking of line.
                process_line(line, replacements, new)

                if not in_code_block and len(line.strip()) == 0:
                    # Outside code blocks we only keep replacement list for one
                    # paragraph, separated by empty line.
                    replacements = []

            # Output leftover page header lines. This could happen if the header
            # is the only thing in the file.
            if len(page_header_lines) > 0:
                for ph_line in page_header_lines:
                    process_line(ph_line, replacements, new)

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
            arg0 = ""
        else:
            arg0 = args[0]
        arg0 = "%s:%d: %s" % (file, lineno, arg0)
        exc.args = (arg0,) + args[1:]
        raise


def parse_autoversion_tag(tag):
    # Returns a structure like this:
    # [
    #     {
    #         "search": For example: "-b %" to match -b parameter with version.
    #         "repo": Git repository whose version should be substituted.
    #         "complain": true/false
    #     },
    #     ...
    # ]

    # Match a string like:
    # <!--AUTOVERSION: "-b %"/integration "integration-%"/integration-->
    # and allow escaped double quotes in the match string (inside double quotes
    # in example).
    tag_match = re.match("^ *<!-- *AUTOVERSION *: *(.*)--> *$", tag)
    if not tag_match:
        raise Exception("Malformed AUTOVERSION tag:\n%s" % tag)
    end_of_whole_tag = tag_match.end(1)

    matcher = re.compile(r'"((?:[^"]|\\")*)"/([-a-z]+)(?:/([-a-z]+))? *')
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
        complain = match.group(3)
        if complain is None or complain == "":
            complain = False
        elif complain == "complain":
            complain = True
        else:
            raise Exception('Replacement flag must be "complain" or nothing')

        if "%" not in expr and not complain:
            raise Exception(
                'Search string "%s" doesn\'t contain at least one \'%%\' (only allowed in "complain" mode)'
                % expr
            )
        parsed.append({"search": expr, "repo": repo, "complain": complain})
    if last_end != end_of_whole_tag:
        raise Exception(
            (
                "AUTOVERSION tag not parsed correctly:\n%s" + "Example of valid tag:\n"
                '<!--AUTOVERSION: "git clone -b %%"/integration "Mender Client %%"/mender "docker version %%"/ignore-->'
            )
            % tag
        )
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
        end = "==============================================================================="
        print(
            (
                'ERROR: Found version-looking string "%s" in documentation line, not covered by any AUTOVERSION expression. '
                + "Original line:\n\n%s\n%s%s\n\n"
                + "AUTOVERSION expressions in effect:\n%s\n\n"
                + "Line after removing all AUTOVERSION matched sections:\n\n%s\n%s%s\n\n"
                + "See README-autoversion.markdown for more information.\n\n%s"
            )
            % (
                match.group(0),
                sep,
                line,
                sep,
                "None"
                if len(replacements) == 0
                else "\n".join(
                    [
                        '"%s"/%s' % (repl["search"], repl["repo"])
                        for repl in replacements
                    ]
                ),
                sep,
                all_removed,
                sep,
                end,
            )
        )
        global ERRORS_FOUND
        ERRORS_FOUND = True

    # If we were not given a file, then we are just doing checking and are done.
    if fd is None:
        return None

    # Now do the replacement and write that.
    all_replaced = do_replacements(line, replacements, just_remove=False)
    fd.write(all_replaced)


def do_replacements(line, replacements, just_remove):
    all_replaced = line
    for search, repo, complain in [
        (repl["search"], repl["repo"], repl["complain"]) for repl in replacements
    ]:
        if len(search.strip()) <= 2:
            raise Exception(
                "Search string needs to be longer/more specific than just '%s'" % search
            )
        escaped = re.escape(search)

        # From re.escape docs:
        # Changed in version 3.7: Only characters that can have special
        # meaning in a regular expression are escaped. As a result, '!',
        # '"', '%', "'", ',', '/', ':', ';', '<', '=', '>', '@', and "`"
        # are no longer escaped.
        if sys.version_info[:3] < (3, 7, 0):
            _percent = "\%"
        else:
            _percent = "%"

        regex = escaped.replace(_percent, VERSION_MATCHER)
        if repo == "lts":
            regex = escaped.replace(_percent, MINOR_VERSIONS_MATCHER)
        if just_remove:
            repl = search.replace("%", "")
        else:
            if repo == "ignore":
                continue
            elif repo == "lts":
                version = get_lts_versions()
            else:
                version = get_version_of(repo)
            if version is None:
                continue
            if complain:
                if IGNORE_COMPLAIN:
                    continue

                if re.search(regex, all_replaced):
                    raise Exception(
                        'Requires manual fixing so it doesn\'t match "complain" expression: "%s":\n%s'
                        % (search.replace('"', '\\"'), line)
                    )
                else:
                    continue
            repl = search.replace("%", version)
        all_replaced = re.sub(regex, repl, all_replaced)
    return all_replaced


def main():
    global MODE
    global INTEGRATION_REPO
    global INTEGRATION_VERSION
    global VERSION_CACHE
    global ERRORS_FOUND

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check that there are no dangling version references",
    )
    parser.add_argument(
        "--update", action="store_true", help="Update all version references"
    )
    parser.add_argument(
        "--ignore-complain", action="store_true", help='Ignore "complain" expressions'
    )
    parser.add_argument(
        "--integration-dir", metavar="DIR", help="Location of integration repository"
    )
    parser.add_argument(
        "--integration-version",
        help="Integration version to update to. Depends on --integration-dir option",
    )
    parser.add_argument(
        "--mender-client-version",
        help="Mender Client version for client only releases to update to",
    )
    parser.add_argument(
        "--meta-mender-version",
        help="meta-mender version to update to (usually a branch)",
    )
    parser.add_argument(
        "--poky-version", help="poky version to update to (usually a branch)"
    )

    parser.add_argument(
        "--mender-ci-workflows-version",
        help="mender-ci-workflows version to update to",
    )
    args = parser.parse_args()

    if args.update and args.check:
        raise Exception("--check and --update are mutually exclusive")
    elif args.update:
        MODE = UPDATE

        if args.integration_version is not None:
            INTEGRATION_REPO = args.integration_dir
            INTEGRATION_VERSION = args.integration_version

        if args.mender_client_version is not None:
            if args.integration_version is not None:
                raise Exception(
                    "--mender-client-version and --integration-version are mutually exclusive"
                )
            VERSION_CACHE["mender"] = args.mender_client_version

        if args.meta_mender_version is not None:
            if args.poky_version is None:
                raise Exception(
                    "--meta-mender-version argument requires --poky-version"
                )
            VERSION_CACHE["meta-mender"] = args.meta_mender_version
            VERSION_CACHE["poky"] = args.poky_version
        else:
            print('Not replacing "meta-mender" instances, since it was not specified')
            print('Not replacing "poky" instances, since it was not specified')
            VERSION_CACHE["meta-mender"] = False
            VERSION_CACHE["poky"] = False
        if args.mender_ci_workflows_version is not None:
            VERSION_CACHE["mender-ci-workflows"] = args.mender_ci_workflows_version

    elif args.check:
        MODE = CHECK
    else:
        raise Exception("Either --check or --update must be given")

    if args.ignore_complain:
        global IGNORE_COMPLAIN
        IGNORE_COMPLAIN = True

    walk_tree()

    if ERRORS_FOUND:
        print("Errors found. See printed messages.")
        sys.exit(1)


if __name__ == "__main__":
    main()
