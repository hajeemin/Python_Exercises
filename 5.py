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

###연습문제 6-4

fav_colors = {
    'Jen':'yellow',
    'Tom' : 'green',
    'sue': 'red',
    'jena': 'blue',
    'julian': 'purple',
}

for name, color in fav_colors.items(): #for문에서 한 세트를 한번에 꺼내는 법! 
    print(f"{name.title()}'s fave color is {color.title()}")

print(fav_colors['Jen'])