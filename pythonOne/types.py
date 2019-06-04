"""
created on 5/20/19
"""
### Imports
from . import program as p
### Functions
def int_(value):
    return str(value)
def float_(value):
    return str(value) + ("f" if p.current_program.lang == "cs" else "")
def bool_(value):
    if p.current_program.lang == "py":
        return "True" if value else "False"
    if p.current_program.lang == "cs":
        return "true" if value else "false"
def str_(value):
    return '"' + value + '"'

def int_type():
    if p.current_program.lang == "py" or p.current_program.lang == "cs":
        return "int"
def bool_type():
    if p.current_program.lang == "py" or p.current_program.lang == "cs":
        return "bool"
def float_type():
    if p.current_program.lang == "py" or p.current_program.lang == "cs":
        return "float"
def str_type():
    if p.current_program.lang == "py":
        return "str"
    if p.current_program.lang == "cs":
        return "string"
def array_type(a_type):
    if p.current_program.lang == "py":
        return "list"
    if p.current_program.lang == "cs":
        return "List<" + a_type + ">"
def empty():
    if p.current_program.lang == "py":
        return "None"
    if p.current_program.lang == "cs":
        return "null"

def to_int(value):
    if p.current_program.lang == "py":
        return "int(" + value + ")"
    if p.current_program.lang == "cs":
        return "Convert.ToInt32(" + value + ")"
def to_float(value):
    if p.current_program.lang == "py":
        return "float(" + value + ")"
    if p.current_program.lang == "cs":
        return "Convert.ToSingle(" + value + ")"
def to_bool(value):
    if p.current_program.lang == "py":
        return "bool(" + value + ")"
    if p.current_program.lang == "cs":
        return "Convert.ToBool(" + value + ")"
def to_str(value):
    if p.current_program.lang == "py":
        return "str(" + value + ")"
    if p.current_program.lang == "cs":
        return "Convert.ToString(" + value + ")"
    