#리스트 공부하기! 리스트에 이번에 배운 f-string이랑 메서드를 사용해봄.

names = ['초파', '현승', '유리', 'elisa']
print(f"나는 강아지를 키운다. 강아지 이름은 {names[0]}이다. 나는 결혼했다. 내 남편의 이름은 {names[1]}이다. 나는 친한 친구가 두 명이 있는데, {names[2]}와 {names[3].title()}이다.")


#리스트 수정하기, 추가.append()하기, 

fruits = ['사과', '바나나', '딸기']
print(fruits)
fruits[0] = '망고'
print(fruits)
fruits.append('포도')
print(fruits)


#인서트 사용하기


#fruits[2].insert('복숭아') 
#print(fruits)
 #인서트 이렇게 했다가 틀림. 올바른 방법 ⬇️

fruits.insert(2,'복숭아')
print(fruits)

#리스트 연습문제

guests = ['현준','지윤','지혜','국범','지우'] #기존 초대 멤버
# print(guests[0]) # 현준이가 갑자기 못온대
# guests[0] = '이진' #이진이로 바꿔
# print(f"안녕~ {guests[0]}! 다음주 토요일 저녁 식사에 초대합니당~")
# print(f"안녕~ {guests[1]}! 다음주 토요일 저녁 식사에 초대합니당~")
# print(f"안녕~ {guests[2]}! 다음주 토요일 저녁 식사에 초대합니당~")
# print(f"안녕~ {guests[3]}! 다음주 토요일 저녁 식사에 초대합니당~")
# print(f"안녕~ {guests[4]}! 다음주 토요일 저녁 식사에 초대합니당~")

# print(f"{guests}, 더 큰 식당을 찾았어염!")

guests.insert(0,'이찬') # 이거 오류 났었는데 고침. 내가 guest = guest.inset()라고 함 ㅜ 앞에 게스트= 이거 왜햇냐!!
guests.insert(3,'성찬') # 리스트 4번째에 추가하기
guests.append('현승') # 마지막에 추가하기
print(guests)


# 팝 쓰는법. 근데 이름으로 찾고싶었는데 그건 안나와서 인터넷에서 찾아봄. index를 사용하면 됨.
cannot = guests.pop(0)
print(f"미안해,{cannot}. 저녁식사에 두명 밖에 초대를 못하게 되어서 우린 다음에 밥을 같이 먹어야할것같아ㅜㅜ")
cannot_02 = guests.pop(guests.index('성찬'))
print(f"미안해,{cannot_02}. 저녁식사에 두명 밖에 초대를 못하게 되어서 우린 다음에 밥을 같이 먹어야할것같아ㅜㅜ")

print(f"{guests}, 너희는 아직 초대되었어. 꼭 와!")

print(guests)
print(f"결국 저녁 식사에는 {len(guests)}명만 와") #len으로 몇명 남았나 알아보기

guests.clear()
print(guests)
