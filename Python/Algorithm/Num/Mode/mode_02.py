import random
import mode_module as mm

scores = random.choices(range(70,101,5),k=100)
print(scores)

# 최빈값
maxAlo = mm.MaxAlgorithm(scores)
maxAlo.setMaxNumIdxAndNum()
maxNum = maxAlo.getMaxNum()
print(maxNum)

# 인덱스 리스트 생성
indexes = [0 for i in range(maxNum + 1)]

for n in scores:
    indexes[n] += 1

n = 1
while True:
    maxAlo = mm.MaxAlgorithm(indexes)
    maxAlo.setMaxNumIdxAndNum()
    maxNum = maxAlo.getMaxNum()
    maxNumIdx = maxAlo.getMaxNumIdx()

    if maxNum == 0:
        break

    print(f'{n}. {maxNumIdx}빈도수: {maxNum}\t', end='')
    print('+'*maxNum)

    indexes[maxNumIdx] = 0
    n += 1