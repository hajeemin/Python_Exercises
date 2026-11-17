#5-8 # 리스트에 원소가 없을때. 출력되게하는 말.
user_names = ['admin','julian']

for user_name in user_names:
    if user_name == 'admin':
        print("안녕하세요 관리자님, 상태 보고?")
    else:
        print(f"안녕 {user_name.title()}! Good to see you again!")

print("사용자가 있어야함")

#이렇게해도 출력이 되는데 

user_names = ['admin','julian']

if user_names: # 유저네임이 있어서 'True'라고 출력되면 밑으로 내려감. 
                #true 안에서 또 돌면서 for, if 문 진행.
    for user_name in user_names:
        if user_name == 'admin':
            print("헬로 관리자님!")
        else:
            print(f"헬로 {user_name}! 다시 와줘서 고마워!")
else:
    print("유저 리스트를 확인해주세요.") 