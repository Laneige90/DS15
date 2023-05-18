# 이진 탐색으로 찾으려는 숫자의 위치 출력

nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
nums.sort()  # 이진 탐색 선행 조건 > 정렬
print(nums)

searchNum = int(input('찾으려는 숫자 입력: '))
searchResult = -1

# 탐색 범위
startIdx = 0  # idx 시작 위치
endIdx = len(nums) -1  # idx 끝 위치
midIdx = (startIdx + endIdx) // 2  # idx 중간 위치
midVal = nums[midIdx]  # 데이터 집합의 중간 위치 값

# 반복문 실행 조건
while searchNum <= nums[len(nums) - 1] and searchNum >= nums[0]:
    # 입력한 숫자가 데이터 집합의 끝의 숫자와 맞았을 때
    # 조건문 실행하지 않고 바로 출력
    if searchNum == nums[len(nums) -1]:
        searchResult = len(nums) -1
        break

    # 입력한 숫자가 중간 값보다 클 시
    if searchNum > midVal:
        startIdx = midIdx
        midIdx = (startIdx + endIdx) // 2
        midVal = nums[midIdx]

    # 입력한 숫자가 중간 값보다 작을 시
    elif searchNum < midVal:
        endIdx = midIdx
        midIdx = (startIdx + endIdx) // 2
        midVal = nums[midIdx]

    # 입력한 숫자가 중간 값과 같을 시
    elif searchNum == midVal:
        searchResult = midIdx
        break

    if searchNum not in nums:
        break

print(searchResult)