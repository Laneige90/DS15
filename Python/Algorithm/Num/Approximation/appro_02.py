import appro_module as am

scores = []

kor = int(input('국어 점수 입력: '))
scores.append(kor)
eng = int(input('영어 점수 입력: '))
scores.append(eng)
math = int(input('수학 점수 입력: '))
scores.append(math)
sci = int(input('과학 점수 입력: '))
scores.append(sci)
his = int(input('역사 점수 입력: '))
scores.append(his)

totalScore = sum(scores)
avgScore = totalScore / len(scores)

print(totalScore)
print(avgScore)

grade = am.getNearNum(avgScore)
print(grade)
