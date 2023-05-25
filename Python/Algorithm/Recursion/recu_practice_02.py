import recu_module as rm

num1 = int(input('숫자 1 입력: '))
num2 = int(input('숫자 2 입력: '))

ns = rm.NumSum(num1, num2)
result = ns.sumBetweenNums()
print('result: {}'.format(result))