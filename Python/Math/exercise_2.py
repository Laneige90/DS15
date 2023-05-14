import random

rNum = random.randint(100,1000)
print(f'rNum : {rNum}')

sisList = []

n = 2
while n <= rNum:
    if rNum % n == 0:
        print(f'소인수 : {n}')
        sisList.append(n)
        rNum /= n
    else:
        n += 1

print(f'sisList : {sisList}')

tempNum = 0
for s in sisList:
    if tempNum != s:
        print(f'{s}\' count : {sisList.count(s)}')
        tempNum = s
