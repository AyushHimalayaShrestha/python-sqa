# lambda+map+filter+reduce
from functools import reduce

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda a, b: a + b, nums)

print(squares, evens, sum_all)
