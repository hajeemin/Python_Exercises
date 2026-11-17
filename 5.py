#5-10

current_users = ['JULIAN','marie','Gemma','jena','jeemin']
new_users = ['tom','Julian','Sue','gemma','hyun','cecil']

current_users_L = [] #전부 소문자로 만들기위한 작업.
for current_user in current_users: #current_users의 이름들을 하나씩 빼서
    current_users_L.append(current_user.lower()) #current_users_L에 소문자 매서드가 적용된 current_user를 추가.
print(current_users_L) #current_user의 소문자 버전의 리스트가 생김.

new_users_L = [] #이것도 마찬가지. new_users의 리스트 원소들을 전부 소문자로 바꾸기 위한 작업. 먼저 빈 리스트를 만듦.
for new_user in new_users: #new_users에 있는 이름들을 하나씩 빼서 new_user로 저장.
    new_users_L.append(new_user.lower()) #new_users_L에 하나씩 .append하면서 마찬가지로 .lower메소드 적용시킴.  
print(new_users_L) #전부 소문자 처리된 new_users_L 리스트가 생겨남.

for new_user_L in new_users_L: #이제 중복된 이름이 있는지 확인. new_users_L에 있는 이름들을 new_user_L로 하나씩 뺌
    if new_user_L in current_users_L: #만약 하나씩 뺀 new_user_L이 current_users_L에 있으면 
        print(f"{new_user_L}>>>이미 등록된 이름입니다. 다른 이름을 입력해주세요.") #중복된 이름이라고 알려줌.
    else: #그게 아니면
        print(f"{new_user_L}>>>사용가능한 이름입니다.") # 사용 가능하다고 알려줌

        #와 이거 존나. 어려웠다 . 