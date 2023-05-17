# 5명 회원가입 및 전체 회원정보 출력

members = {}
n = 1
while n < 6:
    mail = input('메일 입력 : ')
    pw = input('비번 입력 : ')

    if mail in members:
        print('이미 사용 중인 계정 입니다')
    else:
        members[mail] = pw
        n += 1

for key in members.keys():
    print(f'{key} : {members[key]}')

# 특정 회원정보 삭제

while True:
    delMember = input('삭제할 계정 입력 : ')
    if delMember in members:
        delPw = input('비번을 입력해주세요 : ')
        if members[delMember] == delPw:
            del members[delMember]
            print('계정 삭제 완료')
            print(members)
            break
        else:
            print('비번 확인해주세요')


