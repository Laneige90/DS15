def binaryAl(ns, sn):
    searchIdx = -1
    staIdx = 0
    endIdx = len(ns) - 1
    midIdx = (staIdx + endIdx) // 2
    midVal = ns[midIdx]

    print(f'staIdx: {staIdx}, endIdx: {endIdx}')
    print(f'midIdx: {midIdx}, midVal: {midVal}')

    while sn >= ns[0] and sn <= ns[len(ns) - 1]:

        if sn == ns[len(ns) - 1]:
            searchIdx = len(ns) - 1
            break

        if sn > midVal:
            staIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'staIdx: {staIdx}, endIdx: {endIdx}')
            print(f'midIdx: {midIdx}, midVal: {midVal}')

        elif sn < midVal:
            endIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'staIdx: {staIdx}, endIdx: {endIdx}')
            print(f'midIdx: {midIdx}, midVal: {midVal}')

        elif sn == midVal:
            searchIdx = midIdx
            break

    return searchIdx
