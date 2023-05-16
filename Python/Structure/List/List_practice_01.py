# 입력한 정수까지의 약수와 소수 구분
inputNum = int(input('1보다 큰 정수 입력 : '))
list1 = []
list2 = []

for i in range(1,inputNum+1):
    if i == 1:
        list1.append(i)
    else:
        if inputNum % i == 0:
            list1.append(i)

for i in range(2,inputNum+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        list2.append(i)
print(list2)