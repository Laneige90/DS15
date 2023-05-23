def gcd(n1, n2):

    maxNum = 0
    for i in range(1, (n1+1)):
        if n1 % i == 0 and n2 % i == 0:
            maxNum = i

    return maxNum

print(gcd(82, 32))
print(gcd(96, 40))

