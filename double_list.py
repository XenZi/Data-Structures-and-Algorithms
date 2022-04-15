class EmptyList(Exception):
    pass

class Node:

    def __init__(self, value, next, previous):
        self._value = value
        self._next = next
        self._previous = previous
        
    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @value.setter
    def value(self, val):
        self._value = val

    @next.setter
    def next(self, val):
        self._next = val

    @previous.setter
    def previous(self, val):
        self._previous = val
    
    def __str__(self) -> str:
        return f"{self._value}"

class DoubleList():

    def __init__(self):
        self._size = 0
        self._head = Node(None, None, None)
        self._tail = Node(None, None, None)
        self._head.next = self._tail
        self._tail.previous = self._head
    

    '''
        Additional operations:
            - len
            - is_empty
            - first()
            - last()
            - iter
    '''
    def __iter__(self):
        current_node = self._head.next

        while current_node != self._tail:
            yield current_node
            current_node = current_node.next
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        return self._head.next
    
    def last(self):
        return self._tail.previous
    
    '''
        Main operations:
            - add_first
            - add_last
            - remove_first
            - remove_last
            - insert_at
            - get_at
            - remove_at
    '''

    def add_first(self, value):
        node = Node(value, None, None)
        if self.is_empty():
            self._tail.previous = node
        else:
            self._head.next.previous = node
        node.next = self._head.next
        node.previous = self._head
        self._head.next = node
        self._size += 1
    
    def add_last(self, value):
        node = Node(value, None, None)
        if self.is_empty():
            self._head.next = node
        else:
            self._tail.previous.next = node
        node.next = self._tail
        node.previous= self._tail.previous
        self._tail.previous = node
        self._size += 1

    def get_at(self, index):
        if not 0 <= index <= self._size - 1:
            raise IndexError
        counter = 0
        for node in self:
            if counter == index:
                return node
            counter += 1
        return -1

    def remove_first(self):
        if self.is_empty():
            raise EmptyList
        if self._size == 1:
            self._head.next = self._tail
            self._tail.prevous = self._head
        else:
            new_first = self._head.next.next
            self._head.next = new_first
            new_first.previous = self._head
        self._size -= 1
    
    def remove_last(self):
        if self.is_empty():
            raise EmptyList
        if self._size == 1:
            self._tail.previous = self._head
            self._head.next = self._tail
        else:
            new_last = self._tail.previous.previous
            new_last.next = self._tail
            self._tail.previous = new_last
        self._size -= 1
    '''
        Private methods
    '''
    def _insert_after(self, node1, value):
        node = Node(value, None, node1)
        node.next = node1.next
        node1.next.prevous = node
        node1.next = node
        self._size += 1
        return node
    
    def _insert_before(self, node1, value):
        node = Node(value)
        node1.previous.next = node
        node.previous = node1.previous
        node.next = node1
        node1.previous = node
        self._size += 1
        return node
    
    '''
        Public methods
    '''
    def get_at(self, index):
        if not 0 <= index <= self._size:
            raise IndexError("Invalid Index")
        counter = 0
        for node in self:
            if counter == index:
                return node
            counter += 1

    def insert_at(self, index, value):
        if not 0 <= index <= self._size:
            raise IndexError("Invalid Index")
        if index == 0:
            return self.add_first(value)
        if index == self._size:
            return self.add_last(value)
        current_node = self.get_at(index)
        node = self._insert_before(current_node, value)
        self._size += 1
        return node
    
    def remove_at(self, index):
        if not 0 <= index <= self._size - 1:
            raise IndexError("Invalid Index")
        if index == 0:
            return self.remove_first()
        previous_node = self.get_at(index - 1)
        to_remove = previous_node.next
        next_node = previous_node.next.next
        previous_node.next = next_node
        next_node.previous = previous_node
        self._size -= 1
        return to_remove

    def __str__(self) -> str:
        return ", ".join()
    

dlist = DoubleList()

dlist.add_first('a')
dlist.insert_at(1, 'b')
dlist.insert_at(2, 'c')
dlist.add_last('d')


print(dlist.get_at(2))
print(dlist.remove_at(2))
print(dlist.get_at(2))
