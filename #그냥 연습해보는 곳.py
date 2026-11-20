# # # # # # # # #그냥 연습해보는 곳

# # # # # # # # # 확인해야 할 상ㅇ자가 담긴 리스트, 
# # # # # # # # # 확인된 사용자를 저장할 빈 리스트

# # # # # # # # unconfirmed_users = ['alice', 'brian','candace']
# # # # # # # # confirmed_users = []

# # # # # # # # # 확인되지 않은 사용자가 남아잇으면 계속 진행
# # # # # # # # # 확인된 사용자는 해당 리스트로 옮김

# # # # # # # # while unconfirmed_users:
# # # # # # # #     current_user = unconfirmed_users.pop()

# # # # # # # #     print(f"Verifying user: {current_user.title()}")
# # # # # # # #     confirmed_users.append(current_user)

# # # # # # # #     # 확인된 사용자를 모두 표시합니다.

# # # # # # # # print(f"\nThe following users have been confirmed:")
# # # # # # # # for confirmed_user in confirmed_users:
# # # # # # # #     print(confirmed_user.title())

# # # # # # # pets = ['cat', 'dog','cat','pig','cat','rabbit']
# # # # # # # print(pets)

# # # # # # # while 'cat' in pets: #pets 리스트에 'cat'이 있으면 True니까 while 반복. 'cat'이 다 사라지면 False로 루프 멈춤.
# # # # # # #     pets.remove('cat')

# # # # # # # print(pets)


# # # # # # ###########사용자가 입력한 값으로 딕셔너리 채우기 ######################

# # # # # # responses = {}
# # # # # # polling_active = True
# # # # # # while polling_active:
# # # # # #     #참가자의 이름과 응답을 받음
# # # # # #     name = input("\n이름을 입력하세요:")
# # # # # #     response = input("언젠가 어떤 산을 등반하고 싶은가요?")

# # # # # #     responses[name] = response # responses = {name, response}로 쓰면 루프가 돌때마다 새 딕셔너리로 바뀜.

# # # # # #     #설문조사에 참여할 사람이 더 있는지 체크
# # # # # #     repeat = input("설문에 참여할 다른 사람도 있나요? 네/아니오")
# # # # # #     if repeat == '아니오':
# # # # # #         polling_active = False

# # # # # # print("\n ---Poll Results ---")
# # # # # # for name, response in responses.items():
# # # # # #     print(f"{name} 님은 {response} 등반 꼭 이뤄내시길!")

# # # # # # # print(responses)

# # # # # # height = int(input("높이를 입력하세요."))
# # # # # # star = '*'
# # # # # # for star in range(height):
    
# # # # # #     print(star)
# # # # # #     star += 1


# # # # # # star = '*'
# # # # # # num = int(input("숫자를 입력하시오"))

# # # # # # for row in range(1,num+1):
# # # # # #     spaces = " " * (num-row)
# # # # # #     stars = star * (2 * row - 1)
# # # # # #     print(spaces + stars)

























# # # # # star = '*'
# # # # # num = int(input("3이상 숫자를 입력하세요:"))

# # # # # for row in range(1,num+1):
# # # # #     spaces = (" ") * (num - row)
# # # # #     stars = star * (2*row -1)
# # # # #     print(spaces + stars)

# # # # pets = ['cat','dog','rabbit','cat','cow','cat','lizard']
# # # # print(pets)

# # # # while 'cat' in pets:
# # # #     pets.remove('cat')
# # # # print(pets)

# # # def fav_book(book):
# # #     print(f"My favorite book is {book.title()}!!")

# # # fav_book('이상한 나라의 앨리스')

# # def shirts_info(size,message="i love python"):
# #     print(f"Size of a shirts >> {size} \nMessagee on a shirts >> {message}")

# # shirts_info('Medium')
# # shirts_info('Small')
# # shirts_info('Large')

# def describe_city(city,country='Korea'):
#     print(f"{city} is in {country}.")

# describe_city('seoul'.title(),)
# describe_city('daegu'.title(),)
# describe_city('munkyung'.title(),'south korea'.title())

