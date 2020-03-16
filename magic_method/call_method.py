class Hero(object):
    def __init__(self,name):
        print("I am init method")
        self.name=name
    def __call__(self, *args, **kwargs):
        print("I am call method")
        print("I can be called")

if __name__ == '__main__':
    ezreal=Hero("Ezreal")
    ezreal()


