# 시그마
inputA1 = int(input('A1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('N 입력 : '))

valueN = 0; sumN = 0; n = 1

while n <= inputN:
    if n == 1:
        valueN = inputA1
        sumN += valueN
        print('{}번째 항까지의 합 : {}'.format(n, sumN))
        n += 1

    valueN *= inputR
    sumN += valueN
    print('{}번째 항까지의 합 : {}'.format(n, format(sumN,',')))
    n += 1
