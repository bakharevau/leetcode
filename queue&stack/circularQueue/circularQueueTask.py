class MyCircularQueue:

    def __init__(self, k: int):
        self.enqPointer = -1
        self.size = k
        self.elcount = 0
        self.arr = []
        self.head = 0
        self.tail = 0
        for i in range(k):
            self.arr.append(None)

    def enQueue(self, value: int) -> bool:
        if self.elcount == 0:
            self.enqPointer = 0
        else:
            queueHasLastEl = False
            for i in range(self.size - 1):
                if self.arr[i] is not None and self.arr[i + 1] is None:
                    self.enqPointer = i + 1
                    queueHasLastEl = True
                    break
            if not queueHasLastEl:
                for i in range(self.size):
                    if self.arr[i] is None:
                        self.enqPointer = i
        if self.elcount < self.size:
            self.arr[self.enqPointer] = value
            self.tail = self.enqPointer
            self.elcount += 1
            self.enqPointer = -1
            return True
        return False

    def deQueue(self) -> bool:
        if self.elcount > 0:
            self.arr[self.head] = None
            self.elcount -= 1
            if self.head == self.size - 1:
                self.head = 0
            else:
                self.head += 1
            if self.elcount == 0: self.head = 0
            return True
        return False

    def Front(self) -> int:
        if self.elcount > 0:
            return self.arr[self.head]
        return -1

    def Rear(self) -> None:
        if self.elcount > 0:
            return self.arr[self.tail]
        return -1

    def isEmpty(self) -> bool:
        return self.elcount == 0

    def isFull(self) -> bool:
        return self.elcount == self.size