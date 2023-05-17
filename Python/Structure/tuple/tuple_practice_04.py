# 시험 점수 입력 후 튜플에 저장, 및 과목별 학점 출력

korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
mathScore = int(input('수학 점수 입력 : '))
sciScore = int(input('과학 점수 입력 : '))
hisScore = int(input('역사 점수 입력 : '))

scores = (
    {'kor':korScore},
    {'eng':engScore},
    {'math':mathScore},
    {'sci':sciScore},
    {'his':hisScore}
)
for item in scores:
    for key in item.keys():
        if item[key] >= 90:
            item[key] = 'A'
        elif item[key] >= 80:
            item[key] = 'B'
        elif item[key] >= 70:
            item[key] = 'C'
        elif item[key] >= 60:
            item[key] = 'D'
        else:
            item[key] = 'F'

print(scores)