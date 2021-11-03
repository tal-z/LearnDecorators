# Learn About Decorators in Python!

###About
This project is a space for me to learn about python decorators. 
My goal is to write a decorator that adds my signature to a function's docstring.
In the process, I want to fully understand how decorators work. 
I also want to start exploring docstrings, and get a better understanding before trying out sphinx again.

###Findings:
  - Docstrings are easliy accessible at the __doc__ dundermethod
  - Docstrings for Python types are immutable (read-only). Makes sense. 
  - To make decorators work on functions with args and kwargs, 
    you have to pass *args and **kwargs
  - Not sure if the wrapper thing is necessary or just boilerplate in decorators. 
  - Seemingly, I can't use two decorators together. 
    I bet there is a way, though.
  - When you decorate a function, you lose access to the underlying docstring.
    - Why? Well, when you decorate a function, you essentially 
      replace it with a different function that is locally defined. 
      Unless you also define the docstring on that sub-function, 
    - you don't get __doc__ property from the sub-function.
    - You can fix this by explicitly setting the wrapper.__doc__
  - Also noting that it does not seem possible to use 
    multiple decorators on a function, with or without syntactic sugar.


###End Results: 
Success! In main.py, I have a sign_docstring() function 
which, when referenced with a decorator, 
adds my name to the end of a docstring.

There is also a do_twice() function 
which, when referenced with a decorator,
does the function twice. 
I found this on RealPython, and used it as a model. 
I kept it in there, because it offers a simple way 
to demonstrate the two ways of applying decorators in Python, 
and their mutual exclusivity.


