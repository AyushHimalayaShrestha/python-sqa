# Number hourglass fill
n = 5
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(n - i, end=" ")
    print()

for i in range(n-2, -1, -1):
    print(" " * i, end="")
    for j in range(n - i):
        print(n - i, end=" ")
    print()
