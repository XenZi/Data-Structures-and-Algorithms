def selection_sort(array):
    for i in range(len(array)):
        min_i = i
        for j in range(i+1, len(array)):
            if array[min_i] > array[j]:
                min_i = j  
        array[i], array[min_i] = array[min_i], array[i]

if __name__ == "__main__":
    arr = [3,1,2,5,6]
    selection_sort(arr)
    print(arr)