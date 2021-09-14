# Hello BASH!
This is my first set of bash scripts. I learned to make some of them through the Interracting with Python Course of the Google IT Automation with python course on [Coursera](https://www.coursera.org).

Some of the new concepts I used include:
* variables defined by assigning a value to the variable name without a space. For example, `x=1` or `x=y` or `x=<result-of-a-command>` -- I assumed this one. I'm not sure yet. I might have to confirm this myself by making a script that I expect this behaviour from.
* Arithmetic is performed with variables by enclosing them in double parenthesis, as in:
```
((1 + 1)) or (($x + 1)) or (($x + $y))
```
* if conditions, (starting with an `if <condition>; then` statement and closing with a `fi` statement. May also include `else` statements before the `fi` ending).
* `test` command and it's `[ ]` alias. 
    * `-n` for non-zero `STRINGS`s
    * `-le` for comparing `<=`
* `while` loops (starting with a `while <condition>; do` statement and closing with a `done`).
* `for` loops
* command line args accesed through the `$<arg-index>` e.g 
```
command=$1
# This assigns the first command argument
# to command.
```
