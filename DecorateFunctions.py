"""
Main module for learning about decorators
"""

from Decorators import do_twice, sign_docstring, waste_time, timer



# This is how to decorate with syntactic sugar
@timer
@waste_time(10)  # This is a decorator factory
@sign_docstring
@do_twice
def say_hello(name: object) -> object:
    """says hello"""
    print(f"hello {name}")


if __name__ == '__main__':
    # This is how to decorate without syntactic sugar
    #say_hello = Decorators.do_twice(say_hello)
    #say_hello = Decorators.timer(say_hello)
    #say_hello = Decorators.sign_docstring(say_hello)

    say_hello('bill')
    print()

    print("\n\nDOCSTRING:\n__________\n")
    print(say_hello.__doc__)
