# 회원 조회, 로그인 성공 여부, 회원 삭제
# import member_management as mm
#
# mems = mm.MemberRepository()
#
#
# for i in range(3):
#     mId = input('아이디 입력 : ')
#     mPw = input('패스워드 입력 : ')
#
#     mem = mm.Member(mId,mPw)
#     mems.addMember(mem)
#
# mems.printMembers()
#
# mems.loginMember('asd','1234')
# mems.loginMember('zxc','1324')
# mems.loginMember('qwe','1598')
#
# mems.removeMember('asd','1234')
# mems.printMembers()

# Tv class
# import class_TV as cT
#
# my4kTv = cT.Tv4k('65','silver','4K')
# my4kTv.setSmartTv('on')
# my4kTv.turnOn()
# my4kTv.printTvInfo()
# my4kTv.turnOff()
#
# print('-'*60)
#
# my8kTv = cT.Tv8k('75','black','8K')
# my8kTv.setSmartTv('on')
# my8kTv.setAiTv('on')
# my8kTv.turnOn()
# my8kTv.printTvInfo()
# my8kTv.turnOff()

# 자동차 경주
import Racing as rc
import Car

myCarGame = rc.CarRacing()
car01 = Car.CarInfo('Car01','White',250)
car02 = Car.CarInfo('Car02','Red',280)
car03 = Car.CarInfo('Car03','Black',240)
car04 = Car.CarInfo('Car04','Green',260)
car05 = Car.CarInfo('Car05','Yellow',270)

myCarGame.addCar(car01)
myCarGame.addCar(car02)
myCarGame.addCar(car03)
myCarGame.addCar(car04)
myCarGame.addCar(car05)

myCarGame.startRacing()