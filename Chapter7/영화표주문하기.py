prompt = '안녕하세요!'
prompt += '\n나이를 입력해주시면 티켓값을 알려드리겠습니다!'
prompt += '\n나이:'

while True:
    age = int(input(prompt))
    if age < 3:
        print(f"\n****************************\nFor age {age}, it's free!\n****************************\n")
        break
    elif 3<= age <12:
        print(f"\n****************************\nfor age {age}, it's 10 dollars!\n****************************\n")
        break
    elif 12<= age :
        print(f"\n****************************\nfor age {age}, it's 15 dollars!\n****************************\n")
        break
    #여기에 프린트가 들어가면 "이용해주셔서 감사합니다" 출력이 안됨. break에서 빠져나가기 때문. 그래서 와일문 밖으로 빼야함.
print("이용해 주셔서 감사합니다.\n")

##########컨티뉴를 썼을때 무슨 차이가 있을까?#####################

# prompt = '안녕하세요!'
# prompt += '\n나이를 입력해주시면 티켓값을 알려드리겠습니다!'
# prompt += '\n나이:'

# while True:
#     age = int(input(prompt))
#     if age < 3:
#         print(f"\n****************************\nFor age {age}, it's free!\n****************************\n")
#         continue  # 여기에 컨티뉴를 쓰면 계속 무한 반복. 안써도 계속 반복. 
#     elif 3<= age <12:
#         print(f"\n****************************\nfor age {age}, it's 10 dollars!\n****************************\n")
#         continue
#     elif 12<= age :
#         print(f"\n****************************\nfor age {age}, it's 15 dollars!\n****************************\n")
#         continue

# print("이용해주셔서 감사합니다!") 

##########컨티뉴를 빼고 썼을때###################

# prompt = '\n안녕하세요!'
# prompt += '\n나이를 입력해주시면 티켓값을 알려드리겠습니다!'
# prompt += '\n나이:'

# while True:
#     age = int(input(prompt))
#     if age < 3:
#         print(f"\n****************************\nFor age {age}, it's free!\n****************************\n")
         
#     elif 3<= age <12:
#         print(f"\n****************************\nfor age {age}, it's 10 dollars!\n****************************\n")
        
#     elif 12<= age :
#         print(f"\n****************************\nfor age {age}, it's 15 dollars!\n****************************\n")
        
#     print("이용해주셔서 감사합니다!") 
#     ## 이후 무한 반복 나이 묻기. 컨티뉴를 빼면 일단 이용해주셔서 감사합니다는 나옴. 

