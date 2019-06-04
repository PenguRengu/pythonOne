"""
created on 5/20/19
"""
### Variables
current_program = None

### Classes
class Program:
    def __init__(self, lang, options=None):
        if options is None:
            self.options = []
        else:
            self.options = options
        if not (lang in ["py", "cs"]):
            raise ValueError("lang must be set to either \"py\" or \"cs\"")
        self.code = ""
        self.lang = lang
        self.indent = 0
        if self.lang == "py":
            self.add("import pickle")
            self.add("import time")
            self.add("import threading")
            if "ui" in self.options:
                self.add("import tkinter as tk")
                self.add("shapes = []")
    def add(self, line):
        self.code += ("    " * self.indent) + line + "\n"
    def set_current_program(self):
        global current_program
        current_program = self
    def import_(self, other):
        self.code += other.code
    def run(self):
        raise RuntimeError("Don't use run(). Don't ask why.")
        if self.lang != "py":
            raise RuntimeError("lang must be set to \"py\" to run")
        exec(self.code, {}, {})
    def build(self, out_file=None):
        if out_file is None:
            out_file = "output" + (".py" if self.lang == "py" else ".txt")
        with open(out_file, "w") as file:
            file.write(self.code)