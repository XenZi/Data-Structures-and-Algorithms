from queue import Queue

def merge(L, R):
    size_left = len(L)
    size_right = len(R)
    i, j = 0
    sorted = []

    while i < size_left and j < size_right:
        if L[i] < R[j]:
            sorted.append(L[i])
            i += 1
        else:
            sorted.append(R[j])
            j += 1

    if i < size_left:
        sorted.extend(L[i:])
    else:
        sorted.extend(R[j:])
    
    return sorted

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    mid = n // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    return merge(L, R)

def merge_with_queue(S1, S2, S):
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())