# Remarks
This project took months to make despite being a simple password generator. Most of the work done was through refactoring to make the code more readable and maintainable, as well as providing good user experience via the terminal.

## Lessons Learnt
- `Type annotations` can really help one spot bugs in intended program flow, especially as python is dynamically typed.
- Organising functions in the `logical order of dependence` really helps build a reliable mental model of how everything works, with reliable speed.
- Spliting workload into `modular functions` makes it easier to do isolated testing, and helps mark out logical steps to the end goal.
- User of python `linters` and `formatters` to easily make code pretty and catch errors (Pylint, Black, Flake8, Pyright)
- Use of `CONSTANTS` to further improve code logic.
- Use of `docstrings` to improve quick understanding of code.
- Use of `wrapper functions` and `decorators` to extend the functionality of built-in functions, in this case: input()
- Use of `custom Exceptions` to handle the specific exception in my program, in this case: quitting prematurely
- Giving `clear prompts` and `instructions` to users help improve user experience

## Further research:
- Parallelism  (Attempted to use threading to implement the quitting feature but I could not make it work)
- Virtual Environments