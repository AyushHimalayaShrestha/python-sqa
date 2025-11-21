# Hollow butterfly pattern
n = 5
for i in range(1, n+1):
    print("*",end="")
    print(" " * (i-2) + "*" if i>1 else "", end="")
    print(" " * (2*(n-i)), end="")
    print("*" + " " * (i-2) + "*" if i>1 else "*")

for i in range(n-1, 0, -1):
    print("*",end="")
    print(" " * (i-2) + "*" if i>1 else "", end="")
    print(" " * (2*(n-i)), end="")
    print("*" + " " * (i-2) + "*" if i>1 else "*")
