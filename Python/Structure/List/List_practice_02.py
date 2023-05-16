# 1 ~ 100 사이의 난수에서 홀,짝 구분
import random
list1 = []
list2 = []
n = 0
m = 0

for i in range(10):
    numbers = random.randint(1, 100)
    if numbers % 2 == 0:
        list1.append(numbers)
        n += 1
    else:
        list2.append(numbers)
        m += 1

print(f'짝수 : {list1}, 짝수의 개수 : {n}')
print(f'홀수 : {list2}, 홀수의 개수 : {m}')