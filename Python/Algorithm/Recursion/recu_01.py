def recursion(num):

    if num > 0:
        print('*' * num)
        return recursion(num - 1)
    else:
        return 1

recursion(10)