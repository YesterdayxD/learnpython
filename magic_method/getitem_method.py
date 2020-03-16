class MyList(object):
    def __init__(self, length):
        print("I am init method")
        self.myList = [n for n in range(length)]

    def __len__(self):
        return len(self.myList)

    def __getitem__(self, index):
        return self.myList[index]

    def __iter__(self):
        for item in self.myList:
            yield item


if __name__ == '__main__':
    t = MyList(10)
    print("length: ", len(t))
    print(t[8])
    for i in t:
        print(i)
