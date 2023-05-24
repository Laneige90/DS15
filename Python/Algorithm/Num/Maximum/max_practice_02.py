def getAvg(ns):

    total = 0
    for n in ns:
        total += n

    return total / len(ns)

def getMax(ns):

    maxN = ns[0]
    for n in ns:
        if maxN < n:
            maxN = n

    return maxN

def getDiv(n1,n2):
    return round(abs(n1 - n2), 2)

scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70,
          68, 50, 95, 89, 69, 98]

scores_avg = getAvg(scores)
scores_max = getMax(scores)
scores_div = getDiv(scores_max, scores_avg)
print(scores_max)
print(scores_avg)
print(scores_div)