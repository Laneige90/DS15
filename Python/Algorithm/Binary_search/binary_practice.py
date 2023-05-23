import binary_module as bm

if __name__ == '__main__':
    nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    searchNum = int(input('찾을 숫자 입력: '))

    resultIdx = bm.binaryAl(nums, searchNum)
    print(nums)

    if resultIdx == -1:
        print('검색 결과를 찾을 수 없습니다')

    else:
        print('>> 검색 결과 <<')
        print('검색 결과 위치: {}'.format(resultIdx))
        print('검색한 숫자: {}'.format(searchNum))