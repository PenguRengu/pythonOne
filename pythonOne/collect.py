"""
created on 5/24/19
"""
### Imports
from . import program as p

### Functions
def new_array(array_type):
    if p.current_program.lang == "py":
        return "[]"
    if p.current_program.lang == "cs":
        return "new List<" + array_type + ">()"
def add_element(var_name, new_item):
    if p.current_program.lang == "py":
        p.current_program.add(var_name + ".append(" + new_item + ")")
    if p.current_program.lang == "cs":
        p.current_program.add(var_name + ".Add(" + new_item + ");")
def delete_element(var_name, index):
    if p.current_program.lang == "py":
        p.current_program.add("del " + var_name + "[" + index + "]")
    if p.current_program.lang == "cs":
        p.current_program.add(var_name + ".RemoveAt(" + index + ");")
def get_element(var_name, index):
    if p.current_program.lang == "py" or p.current_program.lang == "cs":
        return var_name + "[" + index + "]"