def itemRank(ns):
    rank = []

    for num in ns:
        n = 1
        for j in range(len(ns)):
            if num < ns[j]:
                n += 1
            else:
                continue
        rank.append(n)
    sNum = sorted(ns, reverse=True)
    sRank = sorted(rank)
    print('rank: {}'.format(rank))
    print('sNum: {}'.format(sNum))
    print('sRank: {}'.format(sRank))



