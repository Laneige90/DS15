import random


maxList = random.choices(range(1,10),k=20)
print(maxList)
def MaxNum():
    length = len(maxList)
    max_result = maxList[0]
    for n in range(length):
        if max_result < maxList[n]:
            max_result = maxList[n]
    return max_result

print(f'가장 큰 숫자는 {MaxNum()} 입니다')
maxCnt = maxList.count(MaxNum())
print(f'큰 숫자의 개수는 {maxCnt} 입니다')
