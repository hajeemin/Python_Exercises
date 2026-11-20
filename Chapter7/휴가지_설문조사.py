prompt = "\n이번 휴가철 가장 가고싶은 여행지를 알려주세요!"
prompt += "\n(끝내고싶다면 '종료'를 입력해주세요!)"

message = prompt
#responses = {}
responses = []
while True:
    print(message)
    response = input("휴가철 가장 가고싶은 여행지는?:")
    if response == '종료':
        break
    else:
        #responses.append(response) 5줄에 responses가 딕셔너리라서 .append()메소드가 안먹히는거였음.
        responses.append(response)

print(responses)
