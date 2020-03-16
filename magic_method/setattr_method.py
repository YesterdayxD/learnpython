class Hero(object):
    def __init__(self, name):
        print("I am init method")
        self.name = name

    def __setattr__(self, key, value):
        self.__dict__[key] = value


if __name__ == '__main__':
    ezreal = Hero("Ezreal")
    ezreal.age = 18
    print(ezreal)
