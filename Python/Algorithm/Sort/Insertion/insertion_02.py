import random as rd
import insertion_module as im

nums = rd.choices(range(1,1000),k=100)
print(nums)

numsASC = im.insertionAsc(nums)
print(numsASC)
print(numsASC[0])

numDESC = im.insertionDESC(nums)
print(numDESC)
print(numDESC[0])
