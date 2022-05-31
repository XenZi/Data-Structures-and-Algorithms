from hash_map import HashMap
from map import Map

class ChainedHashMap(HashMap):
    def _bucket_getitem(self, i, key):
        bucket = self._data[i]
        if bucket is None:
            raise KeyError("Key is not found")
        return bucket[key]

    def _bucket_setitem(self, bucket_index, key, value):
        bucket = self._data[bucket_index]
        if bucket is None:
            self._data[bucket_index] = Map()
        current_size = len(self._data[bucket_index])
        self._data[bucket_index][key] = value
        if len(self._data[bucket_index]) > current_size:
            self._size += 1 
    
    def _bucket_delitem(self, bucket_index, key):
        bucket = self._data[bucket_index]
        if bucket is None:
            raise KeyError("Key is not found")
        
        del bucket[key]
    
    def __iter__(self):
        for bucket in self._data:
            if bucket is not None:
                for key in bucket:
                    yield key

    def items(self):
        for bucket in self._data:
            if bucket is not None:
                for (k, v) in bucket.items():
                    yield k, v

        