# Binary Search
def binary_search(arr, x):
    low,high = 0, len(arr) -1
    while low <= high:
        mid = (low+high) //2
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            low = mid + 1
        else:
            high = mid -1
        return -1
nums =[10,20,30,40,50,60,70,80,90]
target= int(input('Enter number to search: '))
result = binary_search(nums, target)
print('Found at index' if result != -1 else "Not Found",result)