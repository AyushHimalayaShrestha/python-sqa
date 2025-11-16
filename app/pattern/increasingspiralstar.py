# Increasing spiral of star
n = 5
size = 2*n - 1

mat = [[" "] * size for _ in range(size)]
top, bottom, left, right = 0, size-1, 0, size-1

star = "*"

while top <= bottom and left <= right:
    for i in range(left, right+1):
        mat[top][i] = star
    for i in range(top, bottom+1):
        mat[i][right] = star
    for i in range(right, left-1, -1):
        mat[bottom][i] = star
    for i in range(bottom, top-1, -1):
        mat[i][left] = star

    top += 2
    bottom -= 2
    left += 2
    right -= 2

for row in mat:
    print("".join(row))
