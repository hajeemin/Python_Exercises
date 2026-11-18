# # 연습문제 6-8

# pets = {
#     'chopa' : 'jeemin',
#     'thunder' : 'jena',
#     'berry' : 'tom',
# }

# for pet_name, owner in pets.items():
#     #print(f"{pet_name}'s owner's name is {owner}.")
#     #print(f"{owner.title()} is the owner of {pet_name.title()}.")
#     print(f"\n{pet_name}:")
#     print(f"{owner}'s dog.")

favorite_places = {
    'jeemin' : ['home'],
    'julian' : ['gym','home'],
    'chopa' : ['han river', 'yangjaecheon','parks'],
    }

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"{name.title()}'s favorite place is {','.join(places)}.")

    else:
        print(f"{name.title()}'s favorite places are {','.join(places)}.")
        