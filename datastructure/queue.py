class Queue(object):
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.length = n
        self.array = [0] * (n + 1)

    def push(self, value):
        if self.tail - self.head == self.length or self.tail - self.head == -1:
            print("queue is full")
            return
        self.array[self.tail] = value
        if self.tail == self.length:
            self.tail = 0
        else:
            self.tail += 1
        pass

    def pop(self):
        if self.tail == self.head:
            print("queue is empty")
            return
        value = self.array[self.head]
        self.array[self.head] = -1
        if self.head == self.length:
            self.head = 0
        else:
            self.head += 1
        print("pop: ", value)
        return value

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False


if __name__ == '__main__':
    q = Queue(5)
    print(q.array, q.head, q.tail)
    print("Is it empty ? {}".format(q.is_empty()))
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    q.pop()
    q.push(6)
    q.pop()
    q.push(7)
    q.pop()
    q.push(8)
    q.pop()
    q.push(9)
    q.pop()
    q.push(10)
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.pop()

    # q.push(11)

    print(q.array, q.head, q.tail)

    pass
