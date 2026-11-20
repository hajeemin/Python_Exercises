#이름까지 같이 받는거 해보기

prompt = "\n이번 휴가철 가장 가고싶은 여행지를 알려주세요!"


message = prompt
responses = {}
#responses = []
while True:
    print(message)
    name = input("이름을 입력해주세요:")
    place = input("휴가철 가장 가고싶은 여행지는?:")
    responses[name] = [place]
    
    response = input("계속 진행하시겠습니까? \n끝내고싶다면 '종료'를 눌러주세요.")
    
    if response == '종료':
        break
    else:
        #responses.append(response) 5줄에 responses가 딕셔너리라서 .append()메소드가 안먹히는거였음.
        continue

print(responses)
