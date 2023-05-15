# 학급 학생 수가 가장 많은 학급과 적은 학급 구분

studentCnt = [['1학급', 18],['2학급',19],['3학급',23],['4학급',21],['5학급',20],['6학급',22],['7학급',17]]

classNum = []
stdCnt = []
for classCnt,cnt in studentCnt:
    classNum.append(classCnt)
    stdCnt.append(cnt)

for i in range(len(studentCnt)):

    if stdCnt[i] == max(stdCnt):
        print(f'학생 수가 가장 많은 학급 : {classNum[i]}({max(stdCnt)})명')

    if stdCnt[i] == min(stdCnt):
        print(f'학생 수가 가장 적은 학급 : {classNum[i]}({min(stdCnt)})명')


