#!/usr/bin/env python2
import re

# --taken from https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
# ----------------------

def applyColor(txt):
  return bcolors.RED + txt.group() + bcolors.ENDC

expression = raw_input('Enter Regex:\n')

text = raw_input('Enter text:\n')

print re.sub(expression, applyColor, text)

## todo: add support for flags
