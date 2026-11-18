# # person_01 = {'first_name':'hyun','last_name':'lee','age':'34','city':'geneve'}
# # print(person_01['first_name'])
# # print(person_01['age'])
# # print(person_01)

# fav_number = {
#     'jen':7,
#     'sue':5,
#     'hyun':8,
#     'jim':2
#     }
# print(f"jim's fav number is {fav_number['jim']}")

# ###연습문제 6-4

# fav_colors = {
#     'Jen':'yellow',
#     'Tom' : 'green',
#     'sue': 'red',
#     'jena': 'blue',
#     'julian': 'purple',
# }

# for name, color in fav_colors.items(): #for문에서 한 세트를 한번에 꺼내는 법! 
#     print(f"{name.title()}'s fave color is {color.title()}")

# print(fav_colors['Jen'])

# 6-5

city_rivers = {
    'korea':'han_river',
    'england':'thames_river',
    'france':'siene_river',
}
for city, river in city_rivers.items():
    if city == 'korea':
        print(f"{river.title()}is the longest river in South Korea.")
    if city == 'england':
        print(f"{river.title()}is the most famous river in England.")
    if city == 'france':
        print(f"{river.title()}is the most famous river in France.")

for city, river in city_rivers.items():
    print(f"{river.title()}")
    print(city)
    #이렇게 뽑으면 강 밑에 나라이름 강, 나라이름 이렇게 나옴. 

for city, river in city_rivers.items():
    print(f"{river.title()}")
          
for city, river in city_rivers.items():
    print(city.title(),end=" ")
    #이렇게 뽑으면 강이름 쫘라락, 나라이름 쫘라락 이렇게 나옴. 