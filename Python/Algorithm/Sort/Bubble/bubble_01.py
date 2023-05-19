nums = [10, 2, 7, 21, 0]

print('정렬 전: {}'.format(nums))

length = len(nums) - 1  # 4 >> 배열은 0부터 시작 (len() 함수는 1부터 셈)
for i in range(length):  # 0 ~ 3 >> 배열 위치 , 배열위치 + 1을 비교하므로 끝까지 갈 필요가 없음
    for j in range(length - i):  # 4-0, 4-1, 4-2, 4-3
        if nums[j] > nums[j + 1]:  # num[j] 가 nums[j+1] 보다 클 때
            nums[j], nums[j + 1] = nums[j + 1], nums[j]  # nums[j], nums[j+1] 자리 교체

print('정렬 후: {}'.format(nums))
