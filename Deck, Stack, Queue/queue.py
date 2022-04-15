'''
    Queue

    - FIFO principle (first-in-first-out)
    - main operations:
        - enqueue(object): adds element on the end of queue
        - dequeue(): removes element from the start of queue
    - additional operations:
        - first(): returns first element without removing
        - len(): returns actual _size of array
        - is_empty(): helps us in edge cases
'''

class EmptyQueue(Exception):
    pass

class Queue:
    def __init__(self):
        DEFAULT_CAPACITY = 10
        self._data = [None] * DEFAULT_CAPACITY
        self._first = 0  # Index of first element in queue
        self._size = 0   # Actual size of queue
 
    def __len__(self):
        return len(self._size)

    def is_empty(self):
        return len(self._size) == 0
    
    def first(self):
        if self.is_empty():
            raise EmptyQueue("Queue is empty")
        return self._first  # we're not returning self._data[0] because it's not being used by the first element all the time, may appear None at this position
    
    def enqueue(self, el):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        el_position = (self._first + self._size) % len(self._data)  # Taking position of the first available element in the Queue
        self._data[el_position] = el
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            return Exception("Empty queue")
        dequeued_el = self._data[self._first] # saving value
        self._data[self._first] = None  # removing actual value with first el index
        self._front = (self._front + 1) % len(self._data)   # let's take for example self._front is 4, so we gonna have 5 % 10 = 5 as first index position
        self._size -= 1
        return dequeued_el

    def _resize(self, cap):
        old_data = self._data   # storing old self._data array with elements in old_data
        self._data = [None] * cap   # creating a new array with new capacity
        walk_element = self._first  # element with which we gonna go through the old data
        for i in range(self._size):
            self._data[i] = old_data[walk_element]  # re-assign value
            walk_element = (1 + walk_element) % len(old_data)
            # actual walk_element is just an index that we use to walk around, for example, if initial value is 5 and for len of old_data is 12, we have: ( 1 + 5 ) % 12 = 6 % 12 = 6, so next indexes are 6, 7, 8, 9, 10, 11, 12
        self._first = 0

    def __str__(self) -> str:
        return str(self._data)

queue = Queue()

for i in range(15):
    queue.enqueue(i)


print(queue)