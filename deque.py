class Empty(Exception):
    ''' Error for empty deque '''

class Deque:
    ''' Implementation of deque '''

    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        ''' Create an empty deque '''
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        ''' Return the number of elements in the deque '''
        return self._size

    def is_empty(self) -> bool:
        ''' Check if the deque is empty '''
        return self._size == 0

    def first(self):
        ''' Return (but do not remove) the first element of the deque '''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        ''' Return (but do not remove) the last element of the deque '''
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, e) -> None:
        ''' Add an element to the front of the deque '''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e) -> None:
        ''' Add an element to the back of the deque '''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def delete_first(self):
        ''' Remove and return the first element of the deque '''
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        ''' Remove and return the last element of the deque '''
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer

    def _resize(self, cap):
        ''' Resize to a new list of capacity >= len(self) '''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self) -> str:
        ''' String representation of the deque '''
        return '[' + ', '.join(str(self._data[(self._front + i) % len(self._data)]) for i in range(self._size)) + ']'


if __name__ == '__main__':
    ''' Local tests for the class '''
    d = Deque()
    print("Deque:", d)
    d.add_first(0)
    d.add_last(1)
    d.add_last(2)
    print("Deque after adding elements:", d)
    print("First element:", d.first())
    print("Last element:", d.last())
    print("Deleted first element:", d.delete_first())
    print("Deleted last element:", d.delete_last())
    print("Deque after removal:", d)
    print("First element:", d.first())
    print("Last element:", d.last())
