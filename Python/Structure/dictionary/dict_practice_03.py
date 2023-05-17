# 문구를 공백으로 구분, 리스트에 저장 후, 인덱스와 단어를 사용해 딕셔너리에 저장

aboutPython = '파이썬은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다'

spList = aboutPython.split()
dict = {}

for i in range(len(spList)):
    dict[i] = spList[i]

print(dict)

# 비속어 -> 표준어 변경 프로그램

words = {
    '꺼지다': '가다',
    '쩔다': '엄청나다',
    '짭새': '경찰관',
    '꼽사리': '중간에 낀 사람',
    '먹튀': '먹고 도망',
    '지린다': '겁을 먹다',
    '쪼개다': '웃다',
    '뒷담 까다': '험담 하다'
}

main = '강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다'
# spList = main.split()

keys = list(words.keys())

for key in keys:
    if key in main:
        print('key : {}'.format(key))
        print('words[{}] : {}'.format(key,words[key]))
        main = main.replace(key, words[key])

print(main)