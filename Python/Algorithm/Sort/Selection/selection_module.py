def selectionASC(ns):
    for i in range(len(ns) -1):
        minIdx = i

        for j in range(i+1, len(ns)):
            if ns[minIdx] > ns[j]:
                minIdx = j

        ns[i], ns[minIdx] = ns[minIdx], ns[i]

    return ns

def selectionDESC(ns):
    for i in range(len(ns) -1):
        minIdx = i

        for j in range(i+1, len(ns)):
            if ns[minIdx] < ns[j]:
                minIdx = j

        ns[i], ns[minIdx] = ns[minIdx], ns[i]

    return ns