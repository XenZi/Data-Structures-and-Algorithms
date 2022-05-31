from hash_map import HashMap
from map import MapElement

class LinearHashMap(HashMap):

    _MARKER = object()

    def _is_available(self, bucket_index):
        return self._data[bucket_index] is None or self._data[bucket_index] is self._MARKER
    
    def _find_bucket(self, bucket_index, key):
        available_slot = None

        while True:
            if self._is_available(bucket_index):
                if available_slot is None:
                    available_slot = bucket_index
                
                if self._data[bucket_index] is None:
                    return False, available_slot
                
            elif key == self._data[bucket_index].key:
                return True, bucket_index
            
            bucket_index = (bucket_index + 1) % len(self._data)

    def _bucket_getitem(self, index, key):
        found, index = self._find_bucket(index, key)
        if not found:
            raise KeyError("Key is not found")
        return self._data[index].value

    def _bucket_setitem(self, index, key, value):
