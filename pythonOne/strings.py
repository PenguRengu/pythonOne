"""
created on 5/27/19
"""
### Imports
from . import program as p
### Functions
def split_(string, sep="' '"):
    if p.current_program.lang == "py":
        return string + ".split(" + sep + ")"
    if p.current_program.lang == "cs":
        return string + ".Split(" + sep + ")"
def substring(string, start, end):
    if p.current_program.lang == "py":
        return string + "[" + start + ":" + end + "]"
    if p.current_program.lang == "cs":
        return string + ".Substring(" + start + ", " + end + ")"