import random

class PrivateBank:  # 개인 통장 클래스

    def __init__(self, bank, account_name):
        self.bank = bank
        self.account_name = account_name
        self.account_no = 0
        self.totalMoney = 0

        while True:
            newAccountNo = random.randint(10000, 99999)
            if bank.isAccount(newAccountNo):  # 계좌번호 유무 체크
                continue                      # 있으면 반복
            else:
                self.account_no = newAccountNo
                break

        self.totalMoney = 0
        bank.addAccount(self)

    def printBankInfo(self):  # 통장 정보 확인 함수
        print('-'*60)
        print(f'account_name : {self.account_name}')
        print(f'account_no : {self.account_no}')
        print(f'totalMoney : {self.totalMoney}')
        print('-'*60)

class Bank:  # 가상의 은행 class

    def __init__(self):
        self.accounts = {}

    def addAccount(self, privateBank):  # 계좌 생성 함수
        self.accounts[privateBank.account_no] = privateBank

    def isAccount(self, ano):  # 기존 계좌 체크 함수
        return ano in self.accounts

    def dodeposit(self, ano, m):  # 입금 함수
        pb = self.accounts[ano]
        pb.totalMoney += m

    def doWithdraw(self, ano, m):  #  출금 함수
        pb = self.accounts[ano]
        if pb.totalMoney - m < 0:
            raise LackException(pb.totalMoney, m)
        pb.totalMoney -= m

class LackException(Exception):  # 잔고 부족 체크 사용자 예외처리 클래스
    def __init__(self, m1, m2):
        super().__init__(f'잔고 부족, 잔액: {m1}, 출금액: {m2} ')
