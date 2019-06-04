# Five-Minute Quickstart
## What's python one?
Python One is a library that can convert python programs to C# (more languages coming soon). An import note is that python one does not run programs like this:
```
Run Statement 1
Run Statement 2
Run Statement 3
```
But like this:
```
Add statement 1 to ouput
Add statement 2 to ouput
Add statement 3 to ouput
Run output
```
## An example
Here's an example program:
```
from pythonOne import *

program = Program("py")
program.set_current_program()

with start():
    printit(str_("Hello World!"))

program.build()
```
Let's break this down.<br>
First you need to import pythonOne:
```
from pythonOne import *
```
Then you need to create a program and set it as the current program:
```
program = Program("py")
program.set_current_program()
```
For the main body of the program you will need have to use the start context manager:
the ``` str ```
