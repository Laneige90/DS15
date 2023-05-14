# 10진수 -> X진수 변환
# dNum = 30
# print('2진수 : {}'.format(bin(dNum)))
# print('8진수 : {}'.format(oct(dNum)))
# print('16진수 : {}'.format(hex(dNum)))

# X진수 -> 10진수 변환
# print('2진수(0b11110) -> 10진수({})'.format(int('0b11110', 2)))
# print('8진수(0o36) -> 10진수({})'.format(int('0o36', 8)))
# print('16진수(0x1e) -> 10진수({})'.format(int('0x1e', 16)))

# 조합 구하기
numN = int(input('첫번째 숫자 입력 : '))
numR = int(input('두번째 숫자 입력 : '))
resultP = 1
resultR = 1
resultC = 1

for i in range(numN, (numN-numR), -1):
    print('N = {}'.format(i))
    resultP *= i
print('resultP = {}'.format(resultP))

for j in range(numR, 0 , -1):
    print('N = {}'.format(j))
    resultR *= j
print('resultR = {}'.format(resultR))

resultC = int(resultP / resultR)
print('resultC = {}'.format(resultC))