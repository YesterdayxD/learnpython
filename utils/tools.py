import time


def time_decorator(a_func):
    def wrap_function(*args, **kwargs):
        start_time = time.time()

        result = a_func(*args, **kwargs)

        end_time = time.time() - start_time

        print("cost_time: {}".format(end_time))

        return result

    return wrap_function


@time_decorator
def test():
    print("hello!")


test()
