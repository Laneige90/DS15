def formatedNumber(n):
    return format(n, ',')

# 단리
def simpleInterest(m, t, r):

    totalM = 0
    totalRateM = 0

    for i in range(t):
        totalRateM += m * (r * 0.01)

    totalM = m + totalRateM
    return int(totalM)

# 월복리
def compoundInterest(m, t, r):

    t = t * 12
    rpm = (r / 12) * 0.01

    totalM = m
    for i in range(t):
        totalM += totalM * rpm

    return int(totalM)
money = int(input('예치금(원) : '))
term =int(input('기간(년) : '))
rate = int(input('연 이율(%) : '))
print('-'* 50)

si = simpleInterest(money, term, rate)
ci = compoundInterest(money, term, rate)
print('[단리 계산기]')
print('-' * 50)
print(f'예치금 : {formatedNumber(money)}원')
print(f'예치기간 : {term}년')
print(f'연 이율 : {rate}%')
print('-' * 50)
print(f'{term}년 후 총 수령액 :{formatedNumber(si)}')
print('-' * 50)
print()

print('[복리 계산기]')
print('-' * 50)
print(f'예치금 : {formatedNumber(money)}원')
print(f'예치기간 : {term}년')
print(f'연 이율 : {rate}%')
print('-' * 50)
print(f'{term}년 후 총 수령액 :{formatedNumber(ci)}')
print('-' * 50)