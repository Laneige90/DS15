studentCnt = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

minClassNo = 0; maxClassNo = 0
minCnt = 0; maxCnt =0

for classNo, cnt in studentCnt:
    if minCnt == 0 or minCnt > cnt:
        minClassNo = classNo
        minCnt = cnt

    if maxCnt < cnt:
        maxClassNo = classNo
        maxCnt = cnt

print('학생 수가 가장 많은 학급 : {}학급 ({}명)'.format(maxClassNo, maxCnt))
print('학생 수가 가장 적은 학급 : {}학급 ({}명)'.format(minClassNo, minCnt))

