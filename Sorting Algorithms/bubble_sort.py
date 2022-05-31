def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

arr = [6,3,1,4,8,9]
bubble_sort(arr)
print(arr)