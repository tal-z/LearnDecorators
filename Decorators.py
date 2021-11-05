import datetime

def do_twice(func):
    def twice_wrapper(*args, **kwargs):
        twice_wrapper.__doc__ = func.__doc__  # Must do this to maintain access to the docstring
        func(*args, **kwargs)
        func(*args, **kwargs)
    return twice_wrapper


def sign_docstring(func):
    def doc_wrapper(*args, **kwargs):
        doc_wrapper.__doc__ = str(func.__doc__) + "\n\nBy: Tal Zaken"
        func(*args, **kwargs)
        print("name:", doc_wrapper.__name__)
    return doc_wrapper


def timer(func):
    def time_wrapper(*args, **kwargs):
        time_wrapper.__doc__ = func.__doc__  # Must do this to maintain access to the docstring
        currrent_time = datetime.datetime.now()
        func(*args, **kwargs)
        runtime = datetime.datetime.now() - currrent_time
        print(func.__name__, f"ran in {runtime.total_seconds()} seconds.")
    return time_wrapper


def waste_time(secs):
    def decorator(func):
        def waste_wrapper(*args, **kwargs):
            import time
            time.sleep(secs)
            return func(*args, **kwargs)
        return waste_wrapper

    return decorator
