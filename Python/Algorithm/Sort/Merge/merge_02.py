def quickSort(ns):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    leftNums, sameNums, rightNums = [], [], []

    for n in ns:
        if n < midVal:
            leftNums.append(n)
        elif n > midVal:
            rightNums.append(n)
        else:
            sameNums.append(n)

    return quickSort(leftNums) + sameNums + quickSort(rightNums)

nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
print(quickSort(nums))