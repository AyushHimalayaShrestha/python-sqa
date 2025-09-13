# check armstrong numbers in range
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    power = len(str(num))
    if sum(int(d) ** power for d in str(num)) == num:
        print(num, end=" ")

