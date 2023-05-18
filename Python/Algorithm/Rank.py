import random

nums = random.sample(range(50,101),20) # 랜덤으로 뽑은 숫자 20개를 리스트 형태로 저장
ranks = [0 for i in range(20)] # 0 20개를 리스트 형태로 저장

for idx, num1 in enumerate(nums): # idx에 인덱스, num1에 숫자 저장
    for num2 in nums: # num2에 nums 숫자 할당
        if num1 < num2: # num1에 할당 된 숫자 보다 num2에 할당된 숫자가 크면
            ranks[idx] += 1 # ranks 리스트의 idx 위치에 있는 0에 1씩 더함

for idx, num in enumerate(nums):
    print(f'number: {num}, rank: {ranks[idx]}')
