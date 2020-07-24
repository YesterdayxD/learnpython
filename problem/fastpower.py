from utils import tools


@tools.time_decorator
def fast_power(b, n):
    result = 1
    for i in range(1, n + 1):
        result = b * result
    return result


a = fast_power(2, 10)
print(a)
