#이름까지 같이 받는거 해보기

message = "\n이번 휴가철 가장 가고싶은 여행지를 알려주세요!"

responses = {}
#responses = []
while True:
    print(message)
    name = input("이름을 입력해주세요:")
    place = input("휴가철 가장 가고싶은 여행지는?:")
    # responses[name] = [place] >>이렇게하면 장소가 리스트에 갇혀서 출력됨.
    responses[name] = place
    
    response = input("계속 진행하시겠습니까? 그렇다면 엔터,\n끝내고싶다면 '종료'를 눌러주세요.")
    
    if response == '종료':
        break
    # else:
        # continue #여기서는 굳이 컨티뉴 필요없음.

print(responses)

