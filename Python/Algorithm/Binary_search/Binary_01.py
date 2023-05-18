datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(datas)
print(len(datas))

searchNum = int(input('찾으려는 숫자 입력: '))
searchIdx = -1

startIdx = 0
endIdx = len(datas) -1
midIdx = (startIdx + endIdx) // 2
midVal = datas[midIdx]

while searchNum <= datas[len(datas)-1] and searchNum >= datas[0]:

    if searchNum > midVal:
        startIdx = midIdx
        midIdx = (startIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchNum < midVal:
        endIdx = midIdx
        midIdx = (startIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchNum == midVal:
        searchResultIdx = midIdx
        break

print(searchResultIdx)