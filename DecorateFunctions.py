"""
Main module for learning about decorators
"""

from Decorators import do_twice, sign_docstring, waste_time, timer

def do_twice(func):
    def twice_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        twice_wrapper.__doc__ = func.__doc__  # Must do this to maintain access to the docstring
        twice_wrapper.__name__ = func.__name__  # Must do this to maintain access to the underlying function name
    return twice_wrapper


# This is how to decorate with syntactic sugar
@timer
@waste_time(5)  # This is a decorator factory
@sign_docstring
@do_twice
def say_hello(name: str):
    """says hello"""
    print(f"hello {name}!")


if __name__ == '__main__':
    # This is how to decorate without syntactic sugar
    #say_hello = do_twice(say_hello)

    say_hello('bunny')

    print()
    print("Docstring")
    print("_________")
    print(say_hello.__doc__)

