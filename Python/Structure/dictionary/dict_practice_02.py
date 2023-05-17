# 삼각형~ 십각형 내각의 합 및 내각 딕셔너리로 저장

# dic = {}
#
# for n in range(3,11):
#     hap = 180 * (n -2)
#     ang = int((hap / n))
#     n = str(n) + '각형'
#     dic[n] = [hap, ang]
#
# print(dic)

# 1부터 10까지의 각각의 정수에 대한 약수를 저장하는 딕셔너리

dict = {}

for i in range(2, 11):
    numList = []
    for j in range(1,i+1):
        if i % j == 0:
            numList.append(j)
    dict[i] = numList

print(dict)
