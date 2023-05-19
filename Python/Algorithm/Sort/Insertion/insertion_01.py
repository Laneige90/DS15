nums = [5, 10, 2, 1, 0]

for i1 in range(1, len(nums)):  # i1 = 1
    i2 = i1 - 1  # i2 = 0
    cNum = nums[i1]  # cNum = nums[1] = 10

    while nums[i2] > cNum and i2 >= 0:  # nums[0] > num[1] and cNum and i2 >= 0
        nums[i2 + 1] = nums[i2] # nums[1] = muns[0]
        i2 -= 1

    nums[i2+1] = cNum

    print(nums)