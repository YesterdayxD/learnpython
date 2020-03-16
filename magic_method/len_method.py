class MyList(object):
    def __init__(self, length):
        print("I am init method")
        self.myList = [0] * length

    def __len__(self):
        return len(self.myList)

    def __getitem__(self, item):
        return self.myList[item]


if __name__ == '__main__':
    t = MyList(10)
    print("length: ", len(t))
    print(t[0])
