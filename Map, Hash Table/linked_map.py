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
    

class MapElement():
    def __init__(self, k, v):
        self._key = k
        self._value = v
    
    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @key.setter
    def key(self, k):
        self._key = k

    @value.setter
    def value(self, v):
        self._value = v

class Map():

    def __init__(self) -> None:
        self._data = DoubleList()
    
    def __getitem__(self, key):
        for item in self._data:
            if key == item.value.key:
                return item.value.value
        raise KeyError(f'There is no element')

    def __setitem__(self, key, value):
        for item in self._data:
            if key == item.value.key:
                item.value.value = value
                return
        self._data.add_last(MapElement(key, value))
    
    def __delitem__(self, key):
        for i in range(len(self._data)):
            if key == self._data[i].key:
                self._data.remove_at(i);
                return
        return KeyError(f'There is no element')
    
    def __iter__(self):
        for item in self._data:
            yield item.value.key
        
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, key):
        for item in self._data:
            if key == item.value.key:
                return True
        return False

    def __iter__(self):
        for item in self._data:
            yield item.value.key

    def items(self):
        for item in self._data:
            yield item.value.key, item.value.value
    
    def keys(self):
        keys = []
        for item in self:
            keys.append(item)
        return keys
    
    def values(self):
        values = []
        for item in self:
            values.append(self[item])
        return values

    def clear(self):
        self._data = []

if __name__=="__main__":
    map = Map()

    map['a'] = 5
    map['b'] = 6
    map['c'] = 7
    map['d'] = 8

    print(map['d'])
    print(map.keys())
    print(map.values())