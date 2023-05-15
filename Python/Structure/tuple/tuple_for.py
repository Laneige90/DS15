minScore = 60
scores = (('국어',70),('영어',65),('음악',45),('과학',59),('사회',80))

for item in scores:
    if item[1] < minScore:
        print('과락 과목 : {}, 점수 : {}'.format(item[0],item[1]))

