nums = [10, 4, 1, 13, 11, 16, 19, 14, 6, 5]

length = len(nums) -1
for i in range(length):
    for j in range(length - i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

    print(nums)