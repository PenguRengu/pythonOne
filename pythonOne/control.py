"""
created on 5/21/19
"""
### Imports
from . import program as p
from contextlib import contextmanager

### Functions
## Condition
@contextmanager
def if_(bool_exp):
    if p.current_program.lang == "py":
        p.current_program.add("if %s:" % bool_exp)
    if p.current_program.lang == "cs":
        p.current_program.add("if (%s) {" % bool_exp)
    p.current_program.indent += 1
    yield
    close()
@contextmanager
def else_if(bool_exp):
    p.current_program.indent -= 1
    if p.current_program.lang == "py":
        p.current_program.add("elif %s:" % bool_exp)
    if p.current_program.lang == "cs":
        p.current_program.add("} else if (%s) {" % bool_exp)
    p.current_program.indent += 1
    yield
    close()
@contextmanager
def else_():
    p.current_program.indent -= 1
    if p.current_program.lang == "py":
        p.current_program.add("else:")
    if p.current_program.lang == "cs":
        p.current_program.add("else {")
    p.current_program.indent += 1
    yield
    close()
## Loops
@contextmanager
def for_(var, times):
    if p.current_program.lang == "py":
        p.current_program.add("for %s in range(%s):" % (var, times))
    if p.current_program.lang == "cs":
        p.current_program.add("for (int " + var + "= 0; " + var + " < " + times + "; " + var + "++) {")
    p.current_program.indent += 1
    yield
    close()
@contextmanager
def while_(condition):
    if p.current_program.lang == "py":
        p.current_program.add("while " + condition + ":")
    if p.current_program.lang == "cs":
        p.current_program.add("while (" + condition + ") {")
    p.current_program.indent += 1
    yield
    close()

## Functions
@contextmanager
def func(name, *args, return_type=None):
    if p.current_program.lang == "py":
        args_string = ""
        for arg in args:
            args_string += arg[1] + ","
        args_string = args_string[:-1]
        p.current_program.add("def " + name + "(" + args_string + "):")
    if p.current_program.lang == "cs":
        args_string = ""
        for arg in args:
            args_string += arg[0] + " " + arg[1] + ","
        args_string = args_string[:-1]
        p.current_program.add("public " + ("static " if not ("ui" in p.current_program.options) else "") + ("void" if return_type is None else return_type) + " " + name + "(" + args_string + ") {")
    p.current_program.indent += 1
    yield
    close()
def call_func(func_name, *args, is_return=False):
    text = func_name + "(" + ",".join(args) + ")"
    if is_return:
        return text
    p.current_program.add(text + (";" if p.current_program.lang == "cs" else ""))

def close():
    p.current_program.indent -= 1
    if p.current_program.lang == "cs":
        p.current_program.add("}")
@contextmanager
def start():
    if p.current_program.lang == "py":
        p.current_program.add("### Main")
        yield
        close()
        return
    if p.current_program.lang == "cs":
        if "ui" in p.current_program.options:
            p.current_program.add("public MainPage() {")
        else:
            p.current_program.add("public static void Main() {")
    p.current_program.indent += 1
    if "ui" in p.current_program.options:
        p.current_program.add("this.InitializeComponent();")
        p.current_program.add("canvas.Background = new SolidColorBrush(Windows.UI.Colors.Transparent);")
        p.current_program.add("canvas.IsTapEnabled = true;")
    yield
    close()