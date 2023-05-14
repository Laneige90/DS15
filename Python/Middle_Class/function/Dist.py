# 이동 거리
# 거리 = 속도 * 시간
def getDistance(speed, hour, minute):
    distance = speed * (hour + minute / 60)
    return distance


print('-' * 50)
s = float(input('속도(km/h) 입력 : '))
h = float(input('시간(h) 입력 : '))
m = float(input('시간(m) 입력 : '))
d = getDistance(s, h, m)
print(f'{s}(km/h)속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리 : {d}(km)')
print('-' * 50)

# 이동 시간
# 시간 = 거리 / 속력
def getTime(speed ,distance):
    time = distance / speed
    print(f'time: {time}')
    h = int(time)
    m = ((time - h) * 100 * 60 / 100)
    return [h, m]

print('-' * 50)
s = float(input('속도(km/h) 입력 : '))
d = float(input('거리(km) 입력 : '))
t = getTime(s, d)
print(f'{s}(km/h) 속도로 {d}(km) 이동한 시간 : {t[0]}(h)시간 {t[1]}(m)분')
print('-' * 50)