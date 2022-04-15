class EmptyList(Exception):
    pass

class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value
    
    @property
    def next(self):
        return self._next
    
    @value.setter
    def value(self, val):
        self._value = val
    
    @next.setter
    def next(self, val):
        self._next = val

    def __str__(self) -> str:
        return f'{self._value}'

class SingleList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    '''
        Additional functions
            - len
            - iter
            - is_empty()
            - first()
            - last()
    '''

    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.next
    
    def first(self):
        if self.is_empty():
            raise EmptyList
        return self._head
    
    def last(self):
        if self.is_empty():
            raise EmptyList
        return self._tail

    '''
        Main functions:
            - add_first()
            - add_last()
            - remove_first()
            - remove_last()
            - remove_at()
            - insert_at()
            - get_at()
    '''

    def add_first(self, value):
        new_node = Node(value) # creating a new node with initial new_node.next = None
        if self.is_empty():
            self._tail = new_node # if list is empty, here we gonna make tail same as the head
        else:
            new_node.next = self._head # if list is not empty, new_node.next is current self._head and it becomes a second element
        self._head = new_node
        self._size += 1
    
    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise EmptyList("List is empty")
        if self._size == 1:
            self._tail = None
        self._head = self._head.next
        self._size -= 1
    
    def remove_last(self):
        if self.is_empty():
            raise EmptyList("List is empty")
        if self._size == 1:
            self._head = None
        for node in self:
            if node.next == self._tail:
                node.next = None
                self._tail = node
                break
        self._size -= 1
    
    def get_at(self, index):
        if not 0 <= index <= self._size - 1:
            raise IndexError
        counter = 0
        for node in self:
            if counter == index:
                return node
            counter += 1
        return -1

    def remove_at(self, index):
        if not 0 <= index <= self._size - 1:
            raise IndexError
        if index == 0:
            self.remove_first()
            return
        if index == self._size - 1:
            self.remove_last()
        previous_node = self.get_at(index - 1)
        previous_node.next = previous_node.next.next
        self._size -= 1

    def insert_at(self, index, value):
        new_value = Node(value)
        if index == 0:
            self.add_first(value)
        if index == self._size - 1:
            self.add_last(value)
        previous_node = self.get_at(index - 1)
        temp = previous_node.next
        previous_node.next = new_value
        new_value.next = temp
        temp = None
        self._size += 1

    def __str__(self) -> str:
        return ", ".join(str(x) for x in self) 

singy = SingleList()

# singy.add_first('b')
# singy.add_first('a')
# singy.add_first('c')
# singy.add_first('d')

# singy.insert_at(3, 'g')
# singy.remove_at(3)
# print(singy.get_at(1))
# print(singy)