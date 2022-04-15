'''
    Double-Ended Queues
    
    - main operations:
        - add_first(object): adds element on the start of queue
        - add_last(object): adds element on the end of queue
        - remove_first(): removes first element from the queue
        - removes_last(): removes last element from the queue
    - additional operations:
        - first(): return the first element of deque
        - last(): return the last element of deque
        - is_empty(): edge cases
        - len(): returns actual _size
'''


class EmptyDeque(Exception):
    pass

class Deque:

    def __init__(self) -> None:
        DEFAULT_CAPACITY = 10
        self._data = [None] * DEFAULT_CAPACITY
        self._first = 0 # index of first
        self._size = 0 # actual size of Deque

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            return EmptyDeque("Empty")
        return self._data[self._first]
    
    def last(self):
        if self.is_empty():
            return EmptyDeque("Empty")
        last_index = (self._first + self._size - 1) % len(self._data) # position of last element
        return self._data[last_index]

    def _resize(self, cap):
        old_data = self._data
        self._data = [None] * cap
        walk = self._first # grabbing actual index of first el.
        for i in range(len(old_data)):
            self._data[i] = old_data[walk]
            walk = (1 + walk) % len(old_data) # walk is index of first that increments, let's take example, walk is 4 and that element is initialized by self._data[i] = old_data[4], now we gonna do (1 + 4) % len(old_data), let's say old_data is 10, 5 % 10 = 5
        self._first = 0 # since we made a new array, _first starts at 0

    def add_first(self, el):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        index = (self._first - 1) % len(self._data) # gets first available index
        self._first = index 
        self._data[index] = el 
        self._size += 1
    
    def add_last(self, el):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        last_index = (self._first + self._size) % len(self._data)
        self._data[last_index] = el
        self._size += 1
    
    def remove_first(self):
        if self.is_empty():
            return EmptyDeque("Empty Deque")
        first_element = self._data[self._first]
        self._data[self._first] = None # 
        self._first = (self._first + 1) % len(self._data)
        self._size -= 1
        return first_element
    
    def remove_last(self):
        if self.is_empty():
            raise EmptyDeque("Empty Deque")
        index = (self._first + self._size - 1) % len(self._data)
        print(index)
        el = self._data[index]
        self._data[index] = None
        self._size -= 1
        return el
    
    def __str__(self) -> str:
        return str(self._data)


deque = Deque()


for i in range(11):
    deque.add_first(i)


# deque.remove_first()
# # print(deque.remove_last())
# deque.add_first(0)
print(deque)
deque.add_last(151)
print(deque.last())
print(deque.first())
print(deque.remove_last())
print(deque.remove_first())
print(deque)
# print(deque.first())
# print(deque.last())
