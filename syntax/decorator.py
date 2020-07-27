def print_hello(str="hello"):
    def wrap_func(fun_a):
        def in_wrap_func(*args, **kwargs):
            print(str)
            return fun_a(*args, **kwargs)

        return in_wrap_func

    return wrap_func


@print_hello(str="fuck")
def test():
    print("world!")


if __name__ == '__main__':
    test()
