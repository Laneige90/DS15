# 찾으려는 숫자 위치 출력
datas = [3,2,5,7,9,1,0,8,6,4]  # 데이터 모음
# print(f'datas: {datas}')
# print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: ')) # 숫자 입력
searchIdx = -1

n = 0
while True:

    if n == len(datas): # n과 datas 길이의 값이 같을 때
        searchIdx = -1 # searchIdx는 -1
        break # 반복문 중단

    elif datas[n] == searchData: # datas[n]의 값과 searchData의 값이 같을 때
        searchIdx = n # searchIdx는 n
        break # 반복문 중단

    n += 1 # 둘 다 해당되지 않을 때 n에 +1

print(f'searchIdx: {searchIdx}')