# aliens=['yellow', 'red','green','blue']

# for alien in aliens:
#     if alien == 'yellow':
#         print(f"{alien} alien.")
#     elif alien == 'red':
#         print(f"{alien} alien.")
#     elif alien == 'blue':
#         print(f"{alien} alien.")
        
pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}

print(f"You've ordered a {pizza['crust']}-crust pizza with the following topings:")
for topping in pizza['toppings']:
    print(topping)

    