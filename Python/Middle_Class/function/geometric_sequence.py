#  등비수열의 n번째 값, 합 출력

def geometric(a1, a2, n):
    add = 0
    for i in range(1,n+1):
        add += a1
        print(f'{i}번째 항의 값 : {a1}')
        a1 *= a2
        print(f'{i}번째 항 까지의 합 : {add}')

num = int(input('a1 입력 : '))
gong = int(input('공비 입력 : '))
n = int(input('n 입력 : '))
print('-' * 50)

seq = geometric(num, gong, n)
