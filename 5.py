# # # 연습문제 6-8

# # pets = {
# #     'chopa' : 'jeemin',
# #     'thunder' : 'jena',
# #     'berry' : 'tom',
# # }

# # for pet_name, owner in pets.items():
# #     #print(f"{pet_name}'s owner's name is {owner}.")
# #     #print(f"{owner.title()} is the owner of {pet_name.title()}.")
# #     print(f"\n{pet_name}:")
# #     print(f"{owner}'s dog.")

# favorite_places = {
#     'jeemin' : ['home'],
#     'julian' : ['gym','home'],
#     'chopa' : ['han river', 'yangjaecheon','parks'],
#     }

# for name, places in favorite_places.items():
#     if len(places) == 1:
#         print(f"{name.title()}'s favorite place is {','.join(places)}.")

#     else:
#         print(f"{name.title()}'s favorite places are {','.join(places)}.")
        
#######################딕셔너리 안에 딕셔너리#####################

# about_cities = {
#     {'seoul':
#     ['population':'500만']
#     ['nation' : 'republic of Korea']
#     ['fact' : 'best people ever']
#     }
# }

# print(f"About city {about_cities{'seoul'['population']}}")


about_cities = {
    'seoul':{
        'nation' : 'south korea',
        'race' : 'asian',
        'fact' : 'best people ever.',
    },
    'paris' : {
        'nation' : 'france',
        'race' : 'white',
        'fact' : 'cool fashion.',

    },
    'milan' : {
        'nation' : 'italy',
        'race' : 'white',
        'fact' : 'not capital.',
    }
}
#print(f"{about_cities['nation']}")
for city_name, city_info in about_cities.items():
    print(f"\nCity name: {city_name.title()}")
    for key,value in city_info.items():
        print(f"\t{key}: {value}")

        #와우 존나 어려웠는데 해냈다!!!!!!!!!!!!!!!!!!