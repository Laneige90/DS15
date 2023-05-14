# 비행기 티켓 영수증 출력

childPrice = 18000
infantPrice = 25000
adultPrice = 50000
DC = 50

def formatNumber(n):
    return format(n, ',')
def airplaneTk(c1,c2,i1,i2,a1,a2):

    cp = c1 * childPrice
    cp_dc = int(c2 * childPrice * 0.5)
    print(f'유아 {c1}명 요금 : {formatNumber(cp)}원')
    print(f'유아 할인 대상 {c2}명 요금 : {formatNumber(cp_dc)}원')

    ip = i1 * infantPrice
    ip_dc = int(i2 * infantPrice * 0.5)
    print(f'소아 {i1}명 요금 : {formatNumber(ip)}원')
    print(f'소아 할인 대상 {i2}명 요금 : {formatNumber(ip_dc)}원')

    ap = a1 * adultPrice
    ap_dc = int(a2 * adultPrice * 0.5)
    print(f'성인 {a1}명 요금 : {formatNumber(ap)}원')
    print(f'성인 할인 대상 {a2}명 요금 : {formatNumber(ap_dc)}원')
    print('-' * 50)

    total = (c1 + c2 + i1 + i2 + a1 + a2)
    total_price = (cp + cp_dc + ip + ip_dc + ap + ap_dc)
    print(f'Total : {total}명')
    print(f'TotalPrice : {formatNumber(total_price)}원')
    print('-' * 50)

childC = int(input('유아 입력 : '))
childDC = int(input('할인대상 유아 입력 : '))

infantC = int(input('소아 입력 : '))
infantDC = int(input('할인대상 소아 입력 : '))

adultC = int(input('성인 입력 : '))
adultDC = int(input('할인대상 성인 입력 : '))
print('-' * 50)

airplaneTk(childC,childDC,infantC,infantDC,adultC,adultDC)