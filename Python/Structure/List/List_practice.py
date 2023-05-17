# 4개 중 2개 선택 경우의 수
numbers = [4,6,7,9]
result = []

# for문 이용
for n1 in numbers:
    for n2 in numbers:
        if n1 == n2:
            continue

        result.append([n1,n2])
print(result)

# 팩토리얼 이용
import math

per = math.factorial(len(numbers)) / math.factorial(len(numbers) - 2)
print(per)
