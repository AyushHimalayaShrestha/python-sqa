n = 5
for i in range(n):
    print(" " * i + "*" + " " * (2*(n-i-1)-1) + ("*" if i != n-1 else ""))
    print()
for i in range(n-2, -1, -1):
    print(" " * i + "*" + " " * (2*(n-i-1)-1) + ("*" if i != n-1 else ""))
