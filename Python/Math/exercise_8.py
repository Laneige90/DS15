# 팩토리얼

# for문 사용
def facFun1(n):

    fac = 1
    for n in range(1,(n+1)):
        fac *= n
    return fac

num = int(input('숫자 입력 : '))
print(f'{num}! : {facFun1(num)} ')

# 재귀함수 사용
def facFun2(n):

    if n == 1:
        return n

    return n * facFun2(n-1)

num = int(input('숫자 입력 : '))
print(f'{num}! : {facFun2(num)} ')

# 라이브러리 사용
import math

num = int(input('숫자 입력 : '))
print(f'{num}! : {math.factorial(num)} ')
