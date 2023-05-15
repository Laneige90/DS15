# 진수 변환
dNum = int(input('10진수 입력 : '))

print('2진수 : {}'.format(bin(dNum)))
print('8진수 : {}'.format(oct(dNum)))
print('16진수 : {}'.format(hex(dNum)))

print('2진수 -> 10진수 : {}'.format(int('0b10110',2)))
print('2진수 -> 10진수 : {}'.format(int('0o14',8)))
print('2진수 -> 10진수 : {}'.format(int('0x2',16)))

print('2진수 -> 8진수 : {}'.format(oct(0b10110)))
print('2진수 -> 10진수 : {}'.format(int(0b10110)))
print('2진수 -> 16진수 : {}'.format(hex(0b10110)))

print('8진수 -> 2진수 : {}'.format(bin(0b10110)))
print('8진수 -> 10진수 : {}'.format(int(0b10110)))
print('8진수 -> 16진수 : {}'.format(hex(0b10110)))

print('16진수 -> 2진수 : {}'.format(bin(0b10110)))
print('16진수 -> 8진수 : {}'.format(oct(0b10110)))
print('16진수 -> 10진수 : {}'.format(int(0b10110)))
