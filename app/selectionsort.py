# Selection Sort
nums = [29, 10, 14, 37, 14]

for i in range(len(nums)):
    min_index = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]

print("Sorted:", nums)
