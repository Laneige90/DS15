import time


def getTime():
    lt = time.localtime()
    st = time.strftime('%Y-%m-%d %H:%M:%S')
    return st


def formatedMoney(n):
    return format(n, ',')


while True:

    selectNumber = int(input('1.입금, 2.출금, 3.종료 '))

    if selectNumber == 1:
        money = int(input('입금액 입력 : '))
        with open('C:/python/bank/money.txt', 'r') as f:
            m = f.read()
        with open('C:/python/bank/money.txt', 'w') as f:
            f.write(str(int(m) + money))

        memo = input('입금 내역 입력 : ')
        with open('C:/python/bank/poketMoney.txt', 'a') as f:
            f.write('-------------------------------\n')
            f.write(f'{getTime()} \n')
            f.write(f'[입금] {memo} : {str(money)}원 \n')
            f.write(f'[잔액] : {str(int(m) + money)}원 \n')
        print('입금 완료')
        print(f'기존 잔액 : {formatedMoney(int(m))}원')
        print(f'입금 후 잔액 : {formatedMoney(int(m) + money)}원')


    elif selectNumber == 2:
        money = int(input('출금액 입력 : '))
        with open('C:/python/bank/money.txt', 'r') as f:
            m = f.read()
        with open('C:/python/bank/money.txt', 'w') as f:
            f.write(str(int(m) - money))

        memo = input('출금 내역 입력 : ')
        with open('C:/python/bank/poketMoney.txt', 'a') as f:
            f.write('-------------------------------\n')
            f.write(f'{getTime()} \n')
            f.write(f'[출금] {memo} : {str(money)}원 \n')
            f.write(f'[잔액] : {str(int(m) - money)}원 \n')
        print('입금 완료')
        print(f'기존 잔액 : {formatedMoney(int(m))}원')
        print(f'출금 후 잔액 : {formatedMoney(int(m) - money)}원')

    elif selectNumber == 3:
        print('종료합니다')
        break
    else:
        print('다시 입력해주세요')
