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
        self._data = []

    
    def __getitem__(self, key):
        for item in self._data:
            if key == item.key:
                return item.value
        raise KeyError(f'There is no element with key {key}')

    def __setitem__(self, key, value):
        for item in self._data:
            if key == item.key:
                item.value = value
                return
        self._data.append(MapElement(key, value))

    def __delitem__(self, key):
        for i in range(len(self._data)):
            if key == self._data[i].key:
                self._data.pop(i)
                return
        return KeyError(f'There is no element with key {key}')
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, key):
        for item in self._data:
            if key == item.key:
                return True
        return False

    def __iter__(self):
        for item in self._data:
            yield item.key
    
    def items(self):
        for item in self._data:
            yield item.key, item.value

    def keys(self):
        keys = []
        for key in self:
            keys.append(key)
        return keys

    def values(self):
        values = []
        for key in self:
            values.append(self[key])
        return values
    
    def clear(self):
        self._data = []


if __name__=="__main__":
    map = Map()

    map['a'] = 5
    map['b'] = 6
    map['c'] = 7
    map['d'] = 8

    del map['c']