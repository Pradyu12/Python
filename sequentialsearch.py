def sequential_search(arr, key):
    for i in range(len(arr)):
            if arr[i] == key:
                return i
            return -1
n = int(input("Enter the number of elements: "))
arr = [ ]
for i in range(n):
    num = int(input(f" Enter element {i+1}: "))
    arr.append(num)
key = int(input("Enter the number to search for: "))
result = sequential_search(arr, key)
if result == -1:
    print(f"{key} was not found in the list.")
else:
    print(f"{key} was found at index {result}.")