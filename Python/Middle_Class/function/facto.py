# 재귀함수 팩토리얼
def formatNum(n):
    return format(n, ',')

def recursionFun(n):
    if n == 1:
        return n

    return n * recursionFun(n-1)

inputNum = int(input('input number : '))
print(formatNum(recursionFun(inputNum)))
