# 합집합, 교집합

tuple1 = (1,3,2,6,12,5,7,8)
tuple2 = (0,5,2,9,8,6,17,3)

hap = list(tuple1)
gyo = list()

for n in tuple2:
    if n not in hap:
        hap.append(n)
    else:
        gyo.append(n)

hap.sort()
gyo.sort()

hap = tuple(hap)
gyo = tuple(gyo)

print(hap)
print(gyo)