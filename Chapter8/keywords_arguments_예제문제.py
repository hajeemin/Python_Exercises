# # def sandwich_orders(*sandwiches_ingredients):
# #     print("Making sandwich with the following ingredients:")
# #     for ingredient in sandwiches_ingredients:
# #         print(f"-{ingredient}")

# # sandwich_orders('tuna')
# # sandwich_orders('ham','cheese')
# # sandwich_orders('avocado','shrimp','lettuce')

# #######위치 인수와 임의의 인수 같이 쓰기##################

# def make_pizza(size, *toppings):
#     print(f"Making {size.title()}-size pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping.title()}")

# make_pizza('small', 'ham','pepper','cheese')
# make_pizza('Large', 'tomato','beef')

#############################임의의 키워드 인수 사용하기##############################
################################키-값 쌍으로 인수 받기!!################################

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein',
#                              location ='prinston',
#                              field = 'physics')

# print(user_profile)



# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first.title()
#     user_info['last_name'] = last.title()
#     return user_info

# user_profile = build_profile('jeemin','ha',
#                             location = 'seoul',
#                             age = 34,
#                             married = 'Yes')

# print(user_profile)

def build_car(company, model_name, **car_info):
    car_info['company_name'] = company.title()
    car_info['car_model'] = model_name.title()
    return car_info
    #return 'company_name', 'car_model'

about_car = build_car('lexus','ux300h',
                      color = 'champaign',
                      sun_roof = 'yes',
                      memory_seat = 'no',
                      )

print(about_car)