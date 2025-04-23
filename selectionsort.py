def selection_sort(arr):
    n = len(arr)
    for i in range(n):
            min = i
            for j in range(i+1, n):
                    if arr [j] < arr [min]:
                            min = j
            arr[i], arr[min] = arr[min], arr[i]
            return arr
n = int (input("Enter the number of elements: "))
arr = [ ]
for i in range(n):
    x = int (input ("Enter element: "))
    arr.append(x)
sorted_arr = selection_sort (arr)
print("Sorted array:", sorted_arr)