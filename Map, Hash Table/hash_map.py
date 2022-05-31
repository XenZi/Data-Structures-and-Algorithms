from random import random, randrange


class HashMap():

    def __init__(self, cap = 10):
        self._data = cap * [None]
        self._capacity = cap
        self._size = 0
        self.prime = 35035153
        self._a = 1 + randrange(self.prime - 1)
        self._b = randrange(self.prime)

    def __len__(self):
        return self._size
    
    def _hash(self, x):
        hashed_value = (hash(x) * self._a + self._b) % self.prime
        compressed = hashed_value % self._capacity
        return compressed
    
    def _resize(self, capacity):
        old_data = list(self.items())
        self._data = capacity * [None]
        self._size = 0

        for (k, v) in old_data:
            self[k] = v
    
    def __getitem__(self, key):
        bucket_index = self._hash(key)
        return self._bucket_getitem(bucket_index, key)

    def __setitem__(self, k, v):
        bucket_index = self._hash(k)
        self._bucket_setitem(bucket_index, k, v)

        if self._size > self._capacity // 2:
            self._resize(2*self._capacity - 1)
    
    def __delitem__(self, k):
        bucket_index = self._hash(k)
        self._bucket_delitem(bucket_index, k)
        self._size -= 1
    
    def items(self):
        raise NotImplementedError()

    def _bucket_getitem(self, index, key):
        raise NotImplementedError()
    
    def _bucket_setitem(self, index, key, value):
        raise NotImplementedError()
    
    def _bucket_delitem(self, index, key):
        raise NotImplementedError()