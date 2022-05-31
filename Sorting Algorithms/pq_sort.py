from pqueue import UnsortedPriorityQueue
from pqueue import SortedPriorityQueue
def unsorted_pq_sort(arr):
    size = len(arr)
    pq = UnsortedPriorityQueue()
    for i in range(size):
        el = arr.pop()
        pq.add(el, el)
    
    for i in range(size):
        (k, v) = pq.remove_min()
        arr.append(v)

def sorted_pq_sort(arr):
    size = len(arr)
    pq = SortedPriorityQueue()

    for i in range(size):
        el = arr.pop()
        pq.add(el, el)
    
    for i in range(size):
        (k, v) = pq.remove_min()
        arr.append(v)

if __name__=="__main__":
    arr_unsorted_first = [6,3,1,4,8,9]
    unsorted_pq_sort(arr_unsorted_first)
    print(arr_unsorted_first)
    arr_unsorted_second = [3,6,1,4,7,2]
    sorted_pq_sort(arr_unsorted_second)
    print(arr_unsorted_second)