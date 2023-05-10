#!/usr/bin/env python3
# the following python scripts extracts bash markdown enclosed in ```bash ```
# and attempts to execute it.
#
# since some manual human interaction is usually required when reading docs,
# you can add custom commands to the markdown using "<!-- AUTOMATION: execute=`whatever`-->"
# to the docs.md file.
#
# if you want to ignore a specific markdown code block, just add <!-- AUTOMATION: ignore=`reason` -->"
# on top of it (note, reason is not required)
#
# if you want need to add a specifc test, just add <!-- AUTOMATION: test=`bash code to test` -->"
#
#
# once all the above is parsed, a shell script is created, and ran.
#
# note that the only command line argument to pass to this script is the docs.md file

import os
import re
import subprocess
import time
from tempfile import NamedTemporaryFile
import sys
import stat

shell_steps = []
ignore_line = "^<!--\s*AUTOMATION:\s*ignore=?.*-->"
execute_line = "^<!--\s*AUTOMATION:\s*execute="
test_line = "^<!--\s*AUTOMATION:\s*test="

ignore_count = 0
execute_count = 0
test_count = 0


if len(sys.argv) == 1:
    print("missing markdown file argument")
    sys.exit(1)


if len(sys.argv) == 2 and sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(
        """
        %s <file>

This tool will parse <file> to extract enclosed ```bash ``` code blocks from markdown,
add it to a shell script, and execute it (with -e -x set).

* Usually when following documentation, some human interaction is required. This can be
  achieved by adding:

      <!-- AUTOMATION: execute=`cmd` -->

  blocks to the markdown file.

* Sometimes, some instructions enclosed in ```bash ``` may not be required and skipped.
  This can be achieved by adding:

      <!-- AUTOMATION: ignore=`reason` -->


* Finally, testing that the instructions executed correctly can be tested using:

      <!-- AUTOMATION: test=`cmd` -->

    """
        % __file__
    )
    sys.exit(0)


with open(sys.argv[1]) as f:
    ignore_next_codeblock = False
    inside_bash_code_block = False
    contents = ""
    for line in f.readlines():
        line = line.strip()
        if line.startswith("git clone"):
            integration_branch = os.environ.get("INTEGRATION_BRANCH")
            if integration_branch is not None:
                default_branch = re.search(r"-b ([a-zA-Z0-9\.\-\_]*) ", line).group(1)
                line = line.replace(default_branch, integration_branch)
                line = line.replace(
                    "github.com/mendersoftware", "gitlab.com/Northern.tech/Mender"
                )
        if re.search(ignore_line, line):
            ignore_next_codeblock = True
            ignore_count += 1
        elif re.search(execute_line, line) or re.search(test_line, line):
            if re.search(execute_line, line):
                cmd = re.sub(execute_line, "", line)
                execute_count += 1
            else:
                cmd = re.sub(test_line, "", line)
                test_count += 1
            cmd = re.sub("\s*-->", "", cmd)
            shell_steps.append(cmd.strip() + os.linesep)
        elif line.startswith("```bash"):
            inside_bash_code_block = True
        elif line.startswith("```") and inside_bash_code_block:
            if ignore_next_codeblock is True:
                ignore_next_codeblock = False
                contents = ""
                inside_bash_code_block = False
            else:
                shell_steps.append(contents)
                contents = ""
                inside_bash_code_block = False
        elif inside_bash_code_block:
            contents += line + os.linesep

with NamedTemporaryFile(dir=os.getcwd(), delete=False) as f:
    f.write(bytes("#!/bin/bash" + os.linesep, "UTF-8"))
    f.write(bytes("set -x -e" + os.linesep, "UTF-8"))
    for line in shell_steps:
        f.write(bytes(line, "UTF-8"))
    os.chmod(f.name, stat.S_IWRITE | stat.S_IREAD | stat.S_IXUSR)

print("Parsing and running: ", sys.argv[1])
print(
    "Total lines ignored: %d\nTotal custom shell commands: %d\nTotal tests to run: %d\n"
    % (ignore_count, execute_count, test_count)
)
time.sleep(3)

ret = subprocess.call(f.name, shell=True)

if ret == 0:
    os.remove(f.name)
else:
    assert False, "shell script extracted from docs failed."
