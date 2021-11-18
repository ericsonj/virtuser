#!/usr/bin/env python3

import subprocess
import os
import sys

env = os.environ.copy()
shell_cmd = sys.argv[1]
env["HOME"] = sys.argv[2]

subprocess.call([shell_cmd], env=env)