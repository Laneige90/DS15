
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

while True:
    print('-'*50)
    cal = input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.종료 : ')

    if cal == '5':
        print('bye~')
        break

    num1 = float(input('첫 번째 숫자 입력 : '))
    num2 = float(input('두 번째 숫자 입력 : '))

    if cal == '1':
        print(f'{num1} + {num2} = {add(num1,num2)}')
    elif cal == '2':
        print(f'{num1} - {num2} = {sub(num1,num2)}')
    elif cal == '3':
        print(f'{num1} X {num2} = {mul(num1,num2)}')
    elif cal == '4':
        print(f'{num1} / {num2} = {div(num1,num2)}')
