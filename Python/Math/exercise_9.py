# 순열
numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

subNum = numN - numR
result = 1
for n in range(numN, subNum, -1):
    print('n : {}'.format(n))
    result *= n

print('result : {}'.format(result))

# 1부터 7까지 카드 7장을 나열하되,
# 2,4,7번 카드가 서로 이웃할 경우의 수

# 2,4,7을 하나의 카드로 생각.
# (2,4,7),1,3,5,6  5장의 순열
num1 = int(input('num1 입력 : '))
result1 = 1
for n in range(num1, 0, -1):
    result1 *= n
print('첫번째 팩토리얼 : {}'.format(result1))

# 2,4,7의 순열
num2 = int(input('num2 입력 : '))
result2 = 1
for n in range(num2, 0, -1):
    result2 *= n
print('두번째 팩토리얼 : {}'.format(result2))

print('결과값 : {}'.format(result1 * result2))
