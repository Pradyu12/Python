def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Better variable name (avoid using 'min' as it's a built-in function)
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr  # Corrected: Now returns after full sorting

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
