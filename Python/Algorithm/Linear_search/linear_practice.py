import random
import linear_module as lm

nums = random.sample(range(1,20),10)
print('숫자 리스트: {}'.format(nums))
searchNum = int(input('찾을 숫자 입력: '))

search = lm.searchNum(nums,searchNum)

if search == -1:
    print('숫자가 목록에 없습니다')
else:
    # print('검색 성공!')
    # print('검색 결과: {}'.format(search))
    print('>> 검색 결과 <<')
    print('검색 결과 위치: {}'.format(search))
    print('검색한 숫자: {}'.format(searchNum))