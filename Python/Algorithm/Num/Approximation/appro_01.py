import random

nums = random.sample(range(0,50), 20)
print(nums)

inputNum = int(input('숫자 입력: '))
print('입력한 숫자: ',inputNum)

nearNum = 0
minNum = 50

for n in nums:
    absNum = abs(n - inputNum)

    if absNum < minNum:
        minNum = absNum
        nearNum = n

print(f'nearNum: {nearNum}')