# CS50 Final Project: Password Generator

### Description
A simple terminal-based password generator that gives you a fair bit of customisation. You can also make a passphrase with this one.

### Getting Started
To get started, run [`project.py`](project.py)

# Contains
### [**Interface**](project.py)
Where you can call the password generators, to provide a password/passphrase for your use.

> **`main()` function**
- Contains a welcome and farewell message. A while loop that gets and provides your password, with another prompt to end the program after generation, or to catch the `QuitCommand` Exception to end it prematurely.

### [**Constants**](constants.py)
- Contains all the CONSTANTS that I've factored out to use across multiple files.

### [**Password Generator**](password_generation.py)
Functions grouped according to their categories.

> **Exceptions**
- Contains the `QuitCommand` custom Exception, meant to signal that the user wants to quit the program.

> **Wrappers**
- Contains the `handle_quit` wrapper for built-in function `input()` via `my_input()` self-declared function. Used to raise `QuitCommand` custom Exception.

> **Helper functions**
- `validate_length()`: Provide simple input validation for password/passphrase length for `get_valid_length()`.
- `get_valid_length()`: Gets the valid length from the user according to `access_key_range` variable.
- `get_character_pool()`: Asks the user for characters to include in their password and include them into the character pool.
- `get_separator()`: Gets a simple separator up to 3 characters in length. Defaults to "_".
- `get_random_uppercase_flag()`: Gets flags from the user for the Random Capitalisation feature for passphrases.
- `randomly_capitalise()`: Randomly capitalises each word according to `get_random_uppercase_flag()`.

> **Main functions**
- `generate_password()`: Prompts the user for features to include in their password and provides them with one.
- `generate_passphrase()`: Prompts the user for features to include in their passphrase and provides them with one.
- `get_access_key()`: Prompts the user to choose between generating a password and a passphrase.

> **Entry Point**
- Contains `main()` that runs only if we are running the library itself. Right now it is the same as `main()` in `password_generation.py`.

### [**Tests**](test_password_generation.py)
- Contains some tests, not fully comprehensive as I do not know how to test password generation.
- Therefore it only contains length validation checks
- Uses pytest with parametrisation