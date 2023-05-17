# 학점 평균

scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))

total = 0
for n1 in scores:
    for n2 in n1:
        total += n2

total = round(total,1)
avg = round(total/ 6, 1)
print(avg)

targetSc = round(4.0 * 8 - total,1)
minScore = targetSc / 2

scores = list(scores)
scores.append((minScore, minScore))

scores = tuple(scores)
print(scores)