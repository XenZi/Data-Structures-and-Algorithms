def insertion_sort(arr):
    size = len(arr)

    for i in range(1, size):
        curr = arr[i]
        j = i-1 #that's why we start from 1

        while j >= 0 and curr < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr

if __name__ == "__main__": 
    arr = [2, 6, 7, 8, 1, 3, 9, 9, 4]
    insertion_sort(arr)
    print(arr)