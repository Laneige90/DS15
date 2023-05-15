# while문을 사용한 학생 수 조회
studentCnt = [['1학급', 18],['2학급',19],['3학급',23],['4학급',21],['5학급',20],['6학급',22],['7학급',17]]

sum = 0
avg = 0
n = 0

while n < len(studentCnt):
    classNum = studentCnt[n][0]
    stdNum = studentCnt[n][1]
    print('{} 학습 학생 수 : {}명'.format(classNum, stdNum))
    sum += stdNum
    n += 1

print('전체 학생 수 : {}명'.format(sum))
print('평균 학생 수 : {}명'.format(sum/(len(studentCnt))))

