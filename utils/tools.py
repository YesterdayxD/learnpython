import time
from functools import wraps


def time_decorator(a_func):
    @wraps(a_func)
    def wrap_function(*args, **kwargs):
        start_time = time.time()

        result = a_func(*args, **kwargs)

        end_time = time.time() - start_time

        print("[Func: {}] cost_time: {}".format(a_func.__name__, end_time))

        return result

    return wrap_function


@time_decorator
def test():
    print("hello!")


if __name__ == '__main__':
    test()
