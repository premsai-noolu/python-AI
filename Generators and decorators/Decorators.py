""" Decorators are described as wrappers that enhance or modify the behavior of functions without altering their core functionality.

Function Wrapping: Decorators allow additional code to run before and after the original function executes. A simple example is given where a decorator logs messages before and after a function runs."""

from functools import wraps
def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("befor function runs")
        func()
        print("after function runs")
    return wrapper


@my_decorator
def greet():
    print("hello world ! how are u")

greet()
print(greet.__name__)