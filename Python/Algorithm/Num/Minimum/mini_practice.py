import random

nums = random.choices(range(1,50), k=30)
print(nums)

def getMin(ns):
    minNum = ns[0]

    for n in ns:
        if minNum > n:
            minNum = n

    return minNum

def minCnt(ns,list):
    cnt = 0
    for n in list:
        if n == ns:
           cnt += 1
    return cnt


minNum = getMin(nums)
print(f'가장 작은 수: {minNum}')
cntMin = minCnt(minNum, nums)
print(f'가장 작은 수의 갯수: {cntMin}')