from utils import tools


@tools.time_decorator
def fast_power(b, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * b % 1000
        n //= 2
        b = b * b % 1000
    return result


if __name__ == '__main__':
    a = fast_power(2, 1000000000)
    # a = fast_power(2, 10)
    print(a)
