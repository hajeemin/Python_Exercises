#5-10

current_users = ['JULIAN','marie','Gemma','jena','jeemin']
new_users = ['tom','Julian','Sue','gemma','hyun','cecil']

current_users_L = []
for current_user in current_users:
    current_users_L.append(current_user.lower())
print(current_users_L)

new_users_L = []
for new_user in new_users:
    new_users_L.append(new_user.lower())
print(new_users_L)

for new_user_L in new_users_L:
    if new_user_L in current_users_L:
        print(f"{new_user_L}>>>이미 등록된 이름입니다. 다른 이름을 입력해주세요.")
    else:
        print(f"{new_user_L}>>>사용가능한 이름입니다.")