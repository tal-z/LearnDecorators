import datetime

def do_twice(func):
    def twice_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        twice_wrapper.__doc__ = func.__doc__  # Must do this to maintain access to the docstring
        twice_wrapper.__name__ = func.__name__  # Must do this to maintain access to the docstring
    return twice_wrapper


def sign_docstring(func):
    def doc_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        doc_wrapper.__doc__ = str(func.__doc__) + "\n\nBy: Tal Zaken"
        doc_wrapper.__name__ = func.__name__
    return doc_wrapper


def timer(func):
    def time_wrapper(*args, **kwargs):
        currrent_time = datetime.datetime.now()
        func(*args, **kwargs)
        time_wrapper.__doc__ = func.__doc__  # Must do this to maintain access to the docstring
        time_wrapper.__name__ = func.__name__  # Must do this to maintain access to the docstring
        runtime = datetime.datetime.now() - currrent_time
        print(func.__name__, f"ran in {runtime.total_seconds()} seconds.")
    return time_wrapper


def waste_time(secs):
    def decorator(func):
        def waste_wrapper(*args, **kwargs):
            import time
            for i in range(secs):
                print(f'{i+1} seconds wasted!')
                time.sleep(1)
            func(*args, **kwargs)
            waste_wrapper.__name__ = func.__name__
            waste_wrapper.__doc__ = func.__doc__
        return waste_wrapper
    return decorator
