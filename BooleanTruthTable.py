# Project Idea: Write a decorator that can be applied to a boolean function,
# which prints out a truth table for the function when it's called.
import itertools
import pandas as pd


def truth_table(func):
    def wrapper(*args, **kwargs):
        num_variables = len(args[0])
        cols = [f'var_{n}' for n in range(1, num_variables + 1)]
        rows = list(itertools.product([0, 1], repeat=num_variables))
        df = pd.DataFrame(data=rows, columns=cols)
        df['f'] = [func(row) for idx, row in df.iterrows()]
        print()
        print(f"Truth Table for {func.__name__}")
        print(df.to_string(index=False))
        print()
        return func(*args)

    return wrapper


@truth_table
def custom_not(values: tuple[bool]):
    return bool(not values[0])


@truth_table
def custom_and(values: tuple[bool, bool]):
    return bool(values[0] and values[1])


@truth_table
def custom_or(values: tuple[bool, bool]):
    return bool(values[0] and not values[1])


@truth_table
def custom_nand(values: tuple[bool, bool]):
    return bool(not (values[0] and values[1]))

@truth_table
def custom_xor(values: tuple[bool, bool]):
    a, b = values
    return bool((a and not b) or (b and not a))


custom_xor([0, 1])
