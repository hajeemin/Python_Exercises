# # # 5-2 연습문제

# # age_01 = 20
# # age_02 = 30

# # print((age_01>30) and (age_02 >= 30))
# # print((age_01>30) or (age_02 >= 30))
# # print((age_01 == 20))
# # print((age_02 != 20))

# travel_items = ['칫솔', '수건','보조배터리', '속옷']
# print('수건' in travel_items)
# print('양말' in travel_items)
# #print('수건','속옷' in travel_items) # 이렇게하니까 안됨
# print('양말'in travel_items and '속옷'in travel_items)


travel_items = ['칫솔', '수건','보조배터리', '속옷']
item = input("제품 잘 챙겼는지 확인해보세요. 제품 입력:")
if item not in travel_items:
    print(f"{item}이 없잖아! 더 잘 신경써서 챙기시오!")
else: print(f"{item} 챙겻으! good!")
