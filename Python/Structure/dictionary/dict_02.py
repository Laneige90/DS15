# dict = {}
#
# dict['이름'] = 'LeeHB'
# dict['전공'] = '소프트웨어'
# dict['메일'] = 'kjw1243@naver.com'
#
# print(dict)

# 0부터 10까지의 팩토리얼을 딕셔너리에 추가
dict = {}

for i in range(11):
    if i == 0:
        dict[i] = 1
    else:
        for j in range(1, (i+1)):
            dict[i] = dict[i - 1] * j

print(dict)
