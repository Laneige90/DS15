studentCnt = [[1, 18],[2,19],[3,23],[4,21],[5,20],[6,22],[7,17]]

minclassNo = 0; maxclassNo = 0
mincnt = 0; maxcnt = 0

n = 0

while n < len(studentCnt):

    if mincnt == 0 or mincnt > studentCnt[n][1]:
        minclassNo = studentCnt[n][0]
        mincnt = studentCnt[n][1]

    if maxcnt < studentCnt[n][1]:
        maxclassNo = studentCnt[n][0]
        maxcnt = studentCnt[n][1]

    n += 1

print('학생 수가 가장 많은 학급 : {}학급 ({}명)'.format(maxclassNo, maxcnt))
print('학생 수가 가장 적은 학급 : {}학급 ({}명)'.format(minclassNo, mincnt))