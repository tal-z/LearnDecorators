"""
Test module for learning about docstrings and imports
"""
def sign_module(module: object) -> object:
    module.__doc__ += "\n\nBy Tal Zaken"
    return module

import DecorateFunctions
main = sign_module(DecorateFunctions)



print(main.__doc__)
