# Map , Filter, Reduce Example
from functools import reduce

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, nums))
evens = list(filter(lambda x: x%2==0, nums))
product = reduce(lambda a, b: a*b, nums)

print("Squares:", squares)
print("Evens:", evens)
print("Product:", product)
