"""
created on 5/20/19
"""
### Imports
from . import program as p
### Functions
## Variables
def new_var(var_name, var_type, var_value):
    if p.current_program.lang == "py":
        p.current_program.add(var_name + " = " + var_value)
    if p.current_program.lang == "cs":
        p.current_program.add("%s %s = %s;" % (var_type, var_name, var_value))
def new_global(var_name, var_type, var_value):
    if p.current_program.lang == "py":
        new_var(var_name, var_type, var_value)
    if p.current_program.lang == "cs":
        p.current_program.add("public " + ("static " if not ("ui" in p.current_program.options) else "") + ("%s %s = %s;" % (var_type, var_name, var_value)))
def set_var(var_name, var_value):
    if p.current_program.lang == "py":
        new_var(var_name, None, var_value)
    if p.current_program.lang == "cs":
        p.current_program.add(var_name + " = " + var_value + ";")
def use_global(var_name):
    if p.current_program.lang == "py":
        p.current_program.add("global " + var_name)

## Math
def op(val1, op, val2):
    return "(" + val1 + " " + op + " " + val2 + ")"

## Built in
def printit(value):
    if p.current_program.lang == "py":
        p.current_program.add("print(" + value + ")")
    if p.current_program.lang == "cs":
        p.current_program.add("Console.WriteLine(" + value + ");")
def read_input():
    if p.current_program.lang == "py":
        return "input()"
    if p.current_program.lang == "cs":
        return "Console.ReadLine()"

