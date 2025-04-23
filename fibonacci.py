N = int (input ("Enter the number you want to check: "))
f3 = 0
f1 = 1
f2 = 1
if (N == 0 or N == 1):
    print("Given number is fibonacci number")
else:
    while f3 < N:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
if f3 == N:
    print("Given number is fibonacci number")
else:
    print("Given number is not a fibonacci number")