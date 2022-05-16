class PQError(Exception):
    pass

class PQItem():

    def __init__(self, k, v):
        self._key = k
        self._value = v
    
    @property
    def key(self):
        return self._key
    @property
    def value(self):
        return self._value
    
    def __lt__(self, x): # less then
        return self._key < x._key   

    def __str__(self) -> str:
        return f'({self._key}, {self._value})'

class PQBase():

    def __init__(self) -> None:
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def __str__(self) -> str:
        return ','.join(str(x) for x in self._data)

class SortedPQ(PQBase):

    def __init__(self) -> None:
        super().__init__()
    
    def min(self):
        if self.is_empty():
            raise PQError("Priority Queue is empty!")
        min_el = self._data[0]
        return (min_el.key, min_el.value)
    
    def remove_min(self):
        if self.is_empty():
            raise PQError("Priority Queue is empty!")
        min_el = self._data.pop(0)
        return (min_el.key, min_el.value)
    
    def add(self, k, v):
        new_item = PQItem(k, v)
        position = 0

        for i in range(len(self) - 1, -1, -1):
            if not new_item < self._data[i]:
                position += 1

        self._data.insert(position, new_item)

class UnsortedPQ(PQBase):
    
    def __init__(self) -> None:
        super().__init__()
    
    def _find_min(self):
        min_el = self._data[0]
        index = 0
        for i in range(len(self._data)):
            if min_el > self._data[i]:
                min_el = self._data[i]
                index = i
        return (min_el, index)
    
    def min(self):
        return self._find_min[0]
    
    def remove_min(self):
        el = self._data.pop(self._find_min()[1])
        return (el.key, el.value)

    def add(self, k, v):
        new_item = PQItem(k, v)
        self._data.append(new_item)

if __name__=="__main__":
    # sqp = SortedPQ()
    # sqp.add(3, "abc")
    # sqp.add(2, "ab")
    # sqp.add(1, "a")
    # sqp.add(11, "abcd")
    # sqp.add(2, "ad")
    # print(sqp)
    # print(sqp.min())
    # print(sqp.remove_min())
    # print(sqp)

    print("---------------")
    uspq = UnsortedPQ()
    uspq.add(3, "abc")
    uspq.add(2, "ab")
    uspq.add(1, "a")
    uspq.add(11, "abcd")
    uspq.add(2, "ad")
    print(uspq.remove_min())
    print(uspq)
    print(uspq.remove_min())
    print(uspq)
    print(uspq.remove_min())

    print("-------SORT-------")