import random
import selection_module as sm

scores = random.choices(range(50,100),k=20)
length = len(scores)

print(f'Length: {length}')

scoreASC = sm.selectionASC(scores)
print(scoreASC)

scoreDESC = sm.selectionDESC(scores)
print(scoreDESC)