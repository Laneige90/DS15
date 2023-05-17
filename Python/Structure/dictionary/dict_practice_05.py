students = {'S21-001': {'이름': '최성훈',
                        '성구분': 'M',
                        '전공': '디자인',
                        '연락처': '010-1234-5678',
                        '메일': 'hun@gmail.com',
                        '취미': ['농구', '음악']},
            'S21-002': {'이름': '탁영우',
                        '성구분': 'M',
                        '전공': '바리스트',
                        '연락처': '010-5678-9012',
                        '메일': 'yeong@gmail.com',
                        '취미': ['축구']},
            'S21-003': {'이름': '황다은',
                        '성구분': 'W',
                        '전공': '음악',
                        '연락처': '010-9012-3456',
                        '메일': 'hunag@gmail.com',
                        '취미': ['수영', '코딩']}
            }

# 전체 학생 정보 출력
# for k1 in students.keys():
#     print('-'*60)
#     print('학생 번호 : {}'.format(k1))
#     student = students[k1]
#     for k2 in student.keys():
#         print('{} : {}'.format(k2,student[k2]))

# 입력한 학생 정보만 출력
studentNo = input('학생 번호 입력 : ')
print('-'*60)
print('학생 번호 : {}'.format(studentNo))
stk = students[studentNo]
for item in stk:
    print('{} : {}'.format(item,stk[item]))
