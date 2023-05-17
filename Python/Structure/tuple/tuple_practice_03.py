# 튜플 슬라이싱

numbers = (8.7, 9.0, 9.1, 9.2, 8.6, 9.3, 7.9, 8.1, 8.3)

# index 0 ~ 3
t1 = numbers[:4]

# index 2 ~ 4
t2 = numbers[2:5]

# index 3 ~
t3 = numbers[3:]

# index 2 ~ -2
t4 = numbers[2:-2]

# index 0 ~ , 3
t5 = numbers[::3]
