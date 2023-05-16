# # del
# memInfo = {'이름':'홍길동','메일':'kjw1243@naver.com','학년':3, '취미':['농구','게임']}
#
# print(memInfo)
#
# del memInfo['메일']
#
# print(memInfo)

# # pop()
# memInfo = {'이름':'홍길동','메일':'kjw1243@naver.com','학년':3, '취미':['농구','게임']}
#
# infoPop = memInfo.pop('이름')
# print(memInfo)
# print(infoPop)

# min score, max score

scores = {'scores1':8.9, 'scores2':8.1, 'scores3':8.5, 'scores4':9.8, 'scores5':8.8,}

minScore = 10; minScoreKey = ''
maxScore = 0; maxScoreKey = ''

for key in scores.keys():

    if scores[key] < minScore:
        minScore = scores[key]
        minScoreKey = key

    if scores[key] > maxScore:
        maxScore = scores[key]
        maxScoreKey = key

del scores[minScoreKey]
del scores[maxScoreKey]

print(scores)