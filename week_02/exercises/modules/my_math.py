# my_module.py
"""This is a simple example module."""

MODULE_VERSION = "1.0" # Module-level variable

def greet(name): # Function definition
    """Greets a person."""
    return f"Hello, {name}! Welcome to my module."

def square_list(numbers): # Another function
    """Squares each number in a list and returns a new list."""
    squared_numbers = [n**2 for n in numbers]
    return squared_numbers