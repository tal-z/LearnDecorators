"""
Main module for learning about decorators
"""

import datetime


class Decorators:

    def do_twice(func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            wrapper.__doc__ = func.__doc__  # Must do this to maintain access to the docstring
            func(*args, **kwargs)
            func(*args, **kwargs)

        return wrapper

    def sign_docstring(func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            wrapper.__doc__ = str(func.__doc__) + "\n\nBy Tal Zaken"
            func(*args, **kwargs)

        return wrapper

    def timer(func):
        def wrapper(*args, **kwargs):
            wrapper.__doc__ = func.__doc__  # Must do this to maintain access to the docstring
            currrent_time = datetime.datetime.now()
            func(*args, **kwargs)
            runtime = datetime.datetime.now() - currrent_time
            print(func.__name__, f"ran in {runtime.total_seconds()} seconds.")

        return wrapper


# This is how to decorate with syntactic sugar
@Decorators.sign_docstring
def say_hello(name: object) -> object:
    """says hello"""
    print(f"hello {name}")


if __name__ == '__main__':
    # This is how to decorate without syntactic sugar
    # say_hello = Decorators.do_twice(say_hello)
    # say_hello = Decorators.timer(say_hello)
    # say_hello = Decorators.sign_docstring(say_hello)

    say_hello('bill')
    print()

    print("\n\nDOCSTRING:\n__________\n")
    print(say_hello.__doc__)
