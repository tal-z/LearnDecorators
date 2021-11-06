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
        print(df)
        return func(*args)
    return wrapper

@truth_table
def custom_bool(vals: list):
    """Custom boolean function"""
    if len([item for item in vals if item == 1]) > len([item for item in vals if item == 0]):
        return True
    else:
        return False

print(custom_bool([0,1,0,1,0]))

