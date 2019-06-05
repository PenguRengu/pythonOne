# Five-Minute Quickstart
## What's python one?
Python One is a library that can convert python programs to C# (more languages coming soon). An import note is that python one does NOT run programs like this:
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
Another important is that because of this, you can't use normal python, but instead you have to use pythonOne's functions.
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
First we import pythonOne:
```
from pythonOne import *
```
Then we create a program and set it as the current program:
```
program = Program("py")
program.set_current_program()
```
If you want to create a program for C#, you would do this:
```
program = Program("cs")
program.set_current_program()
```
For the main body of the program we use the start context manager:
```
with start():
```
Then we print "Hello World!"
```
printit(str_("Hello World!"))
```
The ```str_``` function tells pythonOne that the value is a string.<br>
If you don't use it, and write your code like this:
```
printit("Hello World!")
```
you will get an error when you run the output:
```
  File "output.py", line 5
    print(Hello World!)
                    ^
SyntaxError: invalid syntax
```
Finally, we build the program, which writes its output to output.py (output.txt for languages other than Python):
```
program.build()
```
We can now run this:
```
% python example.py
```
And then run the output:
```
% python output.py
```
