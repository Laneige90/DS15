import copy


def insertionAsc(ns, deepCopy=True):
    if deepCopy:
        cns = copy.copy(ns)
    else:
        cns = ns

    for i1 in range(1, len(cns)):  # i1 = 1
        i2 = i1 - 1  # i2 = 0
        cNum = cns[i1]  # cNum = nums[1] = 10

        while cns[i2] > cNum and i2 >= 0:  # nums[0] > num[1] and cNum and i2 >= 0
            cns[i2 + 1] = cns[i2]  # nums[1] = muns[0]
            i2 -= 1

        cns[i2 + 1] = cNum

    return cns


def insertionDESC(ns, deepCopy=True):
    if deepCopy:
        cns = copy.copy(ns)
    else:
        cns = ns

    for i1 in range(1, len(cns)):  # i1 = 1
        i2 = i1 - 1  # i2 = 0
        cNum = cns[i1]  # cNum = nums[1] = 10

        while cns[i2] < cNum and i2 >= 0:  # nums[0] > num[1] and cNum and i2 >= 0
            cns[i2 + 1] = cns[i2]  # nums[1] = muns[0]
            i2 -= 1

        cns[i2 + 1] = cNum

    return cns
