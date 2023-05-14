import user

# m_name = input('이름 입력 :')
# m_mail = input('메일 입력 :')
# m_pw = input('비밀 번호 입력 :')
# m_addr = input('주소 입력 :')
# m_phone = input('연락처 입력 :')
#
# try:
#     user.checkInput(m_name, m_mail, m_pw, m_addr, m_phone)
#     newMem = user.RegistMember(m_name, m_mail, m_pw, m_addr, m_phone)
#     newMem.printMemberInfo()
# except user.EmptyData as e:
#     print(e)

# import bank
#
# koreaBank = bank.Bank()
#
# new_account_name = input('통장 개설을 위한 예금주 입력 : ')
# my_account = bank.PrivateBank(koreaBank, new_account_name)
# my_account.printBankInfo()
#
# while True:
#     selectNumber = int(input('1.입금,  2.출금,  3.종료'))
#     if selectNumber == 1:
#         m = int(input('입금액 입력 : '))
#         koreaBank.dodeposit(my_account.account_no,m)
#         my_account.printBankInfo()
#
#     elif selectNumber == 2:
#         m = int(input('출금액 입력 : '))
#         try:
#             koreaBank.doWithdraw(my_account.account_no, m)
#
#         except bank.LackException as e:
#             print(e)
#
#         finally:
#             my_account.printBankInfo()
#
#     elif selectNumber == 3:
#         print('Bye~')
#         break
#     else:
#         print('잘못 입력했습니다.  다시 선택하세요')

import calculator as cc

num1 = input('첫 번째 피연산자 입력 : ')
num2 = input('두 번째 피연산자 입력 : ')

# cc.add(num1, num2)
# cc.sub(num1, num2)
# cc.mul(num1, num2)
cc.div(num1, num2)