import random

# choices() 함수 사용
height = random.choices(range(170,186),k=20)

length = len(height) - 1

for i in range(length):
    for j in range(length - i):
        if height[j] > height[j+1]:
            height[j], height[j+1] = height[j+1], height[j]

print(height)
