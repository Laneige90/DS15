nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
indexes = []

n = 0
for i in range(1, (max(nums) + 1)):

    for j in range(max(nums)):

        if i not in nums:
            n = 0
        else:
            n = nums.count(i)

    indexes.append(n)

    print(indexes)


