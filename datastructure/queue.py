class Queue(object):
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.length = n
        self.array = [0] * (n + 1)

    def push(self, value):
        self.tail += 1
        if self.tail > self.length:
            self.tail = 0
        self.array[self.tail] = value
        pass

    def pop(self):
        self.head += 1
        if self.head > self.length:
            self.head = 0
        print("pop: ", self.array[self.head])
        self.array[self.head] = -1
        pass


if __name__ == '__main__':
    q = Queue(5)
    print(q.array, q.head, q.tail)
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    # q.pop()
    # q.push(6)
    # q.pop()
    # q.push(7)
    # q.pop()
    # q.push(8)
    # q.pop()
    # q.push(9)
    # q.pop()
    # q.push(10)
    # q.push(11)

    print(q.array, q.head, q.tail)

    pass
