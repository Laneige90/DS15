# 100부터 1000사이의 난수에 대해 약수 소수 소인수 출력

import random
rNum = random.randint(100,1000)
print(f'rNum : {rNum}')

for num in range(1,rNum+1):
    sisFlag = 0

# 약수
    if rNum % num == 0:
        print(f'약수 : {num}')
        sisFlag += 1

# 소수
    if num != 1:
        flag = True
        for n in range(2,num):
            if num % n == 0:
                flag = False
                break

        if(flag):
            print(f'소수 : {num}')
            sisFlag += 1
# 소인수
    if sisFlag >= 2:
        print(f'소인수 : {num}')
