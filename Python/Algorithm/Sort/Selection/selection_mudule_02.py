def sortSelect(ns):
    for i in range(len(ns)-1):
        numIdx = i

        for j in range(i+1, len(ns)):
            if ns[numIdx] > ns[j]:
                numIdx = j

        ns[i], ns[numIdx] = ns[numIdx], ns[i]
        print(ns)
