# Linear Search in List
nums = [10,20,30,40,50,60,70,80]
x = int(input('Enter number to search: '))

if  x in nums:
    print(x, 'found at index',nums.index(x))
else:
    print(x,'not found')