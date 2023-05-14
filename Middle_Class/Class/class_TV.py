# Tv class - 객체 생성 후 상속
class NormalTv: # 기본 TV 클래스

    def __init__(self, i=32, c='black',r='full-HD'): # 속성
        self.inch = i
        self.color = c
        self.resolution = r
        self.smartTv = 'off'
        self.aiTv = 'off'

    def turnOn(self):  # 기능1
        print('TV power on')

    def turnOff(self): # 기능2
        print('TV power off')

    def printTvInfo(self): # Tv 정보 출력
        print(f'inch : {self.inch}inch')
        print(f'color : {self.color}')
        print(f'resolution : {self.resolution}')
        print(f'smartTv: {self.smartTv}')
        print(f'aiTv : {self.aiTv}')

class Tv4k(NormalTv): # 기본 Tv 클래스 상속1
    def __init__(self, i, c, r='4K'):
        super().__init__(i,c,r)
    def setSmartTv(self,s):
        self.smartTv = s

class Tv8k(NormalTv): # 기본 Tv 클래스 상속2
    def __init__(self, i, c, r='8K'):
        super().__init__(i,c,r)
    def setSmartTv(self,s):
        self.smartTv = s
    def setAiTv(self,a):
        self.aiTv = a