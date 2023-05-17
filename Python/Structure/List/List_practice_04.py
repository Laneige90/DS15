# 리스트 내부 중복 숫자 제거
numbers = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print(f'numbers = {numbers}')

newNumbers = []
for i in range(len(numbers)):
    for num in numbers:
        if num in newNumbers:
            continue
        else:
            newNumbers.append(num)

print(newNumbers)