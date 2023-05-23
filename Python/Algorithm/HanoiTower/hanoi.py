def hanoiTower(discCnt, fromBar, toBar, viaBar):  # 원판 개수, 출발 기둥, 도착 기둥, 경유 기둥
    if discCnt == 1:
        print(f'{discCnt}디스크를 {fromBar}에서 {toBar}(으)로 이동')
    else:
        hanoiTower(discCnt-1, fromBar, viaBar, toBar)
        print(f'{discCnt}디스크를 {fromBar}에서 {toBar}(으)로 이동')
        hanoiTower(discCnt-1, viaBar, toBar, fromBar)

hanoiTower(3,1,3,2)
