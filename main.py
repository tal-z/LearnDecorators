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


# This is how to decorate with syntactic sugar
# @sign_docstring
def say_hello(name):
    """says hello"""
    print(f"hello {name}")


# This is how to decorate without syntactic sugar
say_hello = do_twice(say_hello)

say_hello('bill')

print("\n\nDOCSTRING:\n__________\n")
print(say_hello.__doc__)
