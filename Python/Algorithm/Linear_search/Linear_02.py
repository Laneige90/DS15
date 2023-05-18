# 가장 앞에 있는 7을 검색 후 위치 출력
# nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
#
# idx = 0
#
# searchNum = int(input('검색할 숫자 입력: '))
#
# n = 0
#
# while True:
#     if searchNum == nums[n]:
#         idx = n
#         break
#     n += 1
#
# print('가장 앞에 있는 7의 위치: {}'.format(idx))

# 숫자 7 모두 검색 후 각각의 위치 및 전체 갯수 출력

nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(nums)
searchNum = int(input('찾을 숫자 입력: '))

searchIdx = 0
count = 0
idx = []
n = 0

while True:
    if n == len(nums):
        break
    elif searchNum == nums[n]:
        count += 1
        searchIdx = n
        idx.append(searchIdx)
    n += 1

print(f'{searchNum}의 개수: {count}, {searchNum}의 위치 {idx}')
