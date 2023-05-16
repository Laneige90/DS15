# dict = {}
#
# dict['이름'] = 'LeeHB'
# dict['전공'] = '소프트웨어'
# dict['메일'] = 'kjw1243@naver.com'
#
# dict['이름'] = '홍길동'
#
# print(dict)

# 몸무게 , 신장, BMI 
myBodyInfo = {'이름':'gildong', '몸무게':83.0, '신장':1.8}
myBmi = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)
print(myBodyInfo)
print(round(myBmi, 2))

n = 0
while n < 30:
    myBodyInfo['몸무게'] -= 0.3
    myBodyInfo['신장'] += 0.001
    n += 1
myBodyInfo['몸무게'] = round(myBodyInfo['몸무게'],2)
myBodyInfo['신장'] = round(myBodyInfo['신장'],2)

print(myBodyInfo)
myBmi = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)
print(round(myBmi, 2))

