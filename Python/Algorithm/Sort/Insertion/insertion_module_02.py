import copy
def sortInsert(ns, asc=True):
    c_ns = copy.copy(ns)

    for i1 in range(1,len(c_ns)):
        i2 = i1 -1
        c_Num = c_ns[i1]

        if asc:
            while c_ns[i2] > c_Num and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        else:
            while c_ns[i2] < c_Num and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        c_ns[i2 + 1] = c_Num
    return c_ns