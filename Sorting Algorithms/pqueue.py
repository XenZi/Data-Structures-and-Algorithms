class PQError(Exception):
    pass


class PQItem(object):
    __slots__ = '_key', '_value'

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value

    def __lt__(self, x):
        return self._key < x._key

    def __str__(self):
        return "(" + str(self._key) + ")"


class PriorityQueueBase(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return ', '.join('(%s, %s)' % (e._key, e._value) for e in self._data)

    def is_empty(self):
        return len(self) == 0


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        super().__init__()

    def min(self):

        if self.is_empty():
            raise PQError('Red je prazan.')

        min_item = self._data[0]
        return (min_item._key, min_item._value)

    def remove_min(self):
        if self.is_empty():
            raise PQError('Red je prazan.')

        removed = self._data.pop(0)
        return (removed._key, removed._value)

    def add(self, key, value):
        new_item = PQItem(key, value)

        last = len(self)-1
        position = 0

        for i in range(last, -1, -1):
            current_item = self._data[i]
            if not new_item < current_item:
                position = i+1
                break
        self._data.insert(position, new_item)


class UnsortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        super(UnsortedPriorityQueue, self).__init__()

    def _find_min(self):

        if self.is_empty():
            raise PQError('Red je prazan.')

        min_item = self._data[0]
        size = len(self)
        for i in range(1, size):
            current_item = self._data[i]
            if current_item < min_item:
                min_item = current_item

        return min_item

    def min(self):

        min_item = self._find_min()
        return (min_item._key, min_item._value)

    def remove_min(self):

        min_item = self._find_min()
        index = self._data.index(min_item)
        removed = self._data.pop(index)
        return (removed._key, removed._value)

    def add(self, key, value):
        new_item = PQItem(key, value)
        self._data.append(new_item)
