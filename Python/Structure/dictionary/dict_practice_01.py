# 과목별 점수 저장 및 출력
# subject = ['국어', '영어', '수학', '과학', '국사']
# scores = {}
#
# for s in subject:
#     score = input(s + '점수 입력 : ')
#     scores[s] = score  # item 추가
#
# print('과목별 점수 : {}'.format(scores))

# 아이디, 비밀번호 확인
members = {'urkpo':'0298^7$','xxayv':'%2*9$91','lsqvx':'!0%)&&4'}

memId = input('아이디 입력 : ')
memPw = input('비밀번호 입력 : ')
if memId in members:
    if members[memId] == memPw:
        print('로그인 성공')
    else:
        print('비밀번호 확인')
else:
    print('아이디 확인')
