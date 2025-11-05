# Alphabet Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(65, 65 + i):
        print(chr(j), end="")
    for j in range(65 + i - 2, 64, -1):
        print(chr(j), end="")
    print()
