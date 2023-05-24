def getMinScore(ls):
    minScore = ls[0]
    for n in ls:
        if minScore > n:
            minScore = n
    return minScore

def getAvg(ls):
    total = 0
    for n in ls:
        total += n
    avgScore = total / len(ls)
    return avgScore

def getDiv(n1, n2):
    divScore = round(abs(n1 - n2),2)
    return divScore
scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70,
          68, 50, 95, 89, 69, 98]

minScore = getMinScore(scores)
print(minScore)
avgScore = getAvg(scores)
print(avgScore)
divScore = getDiv(minScore,avgScore)
print(divScore)
