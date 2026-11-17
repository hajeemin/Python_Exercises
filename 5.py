#5-8
user_names = ['admin','julian','jeemin']

for user_name in user_names:
    if user_name == 'admin':
        print("안녕하세요 관리자님, 상태 보고?")
    else:
        print(f"안녕 {user_name.title()}! Good to see you again!")