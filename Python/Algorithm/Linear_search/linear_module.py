def searchNum(datas, searchData):
    searchIdx = -1
    n = 0
    while True:
        if n == len(datas):
            searchIdx = -1
            break
        elif datas[n] == searchData:
            searchIdx = n
            print('검색 성공!')
            print('검색 결과: {}'.format(searchIdx))
            break

        n += 1

    return searchIdx
