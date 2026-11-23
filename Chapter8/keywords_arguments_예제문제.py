# def sandwich_orders(*sandwiches_ingredients):
#     print("Making sandwich with the following ingredients:")
#     for ingredient in sandwiches_ingredients:
#         print(f"-{ingredient}")

# sandwich_orders('tuna')
# sandwich_orders('ham','cheese')
# sandwich_orders('avocado','shrimp','lettuce')

#######위치 인수와 임의의 인수 같이 쓰기##################

def make_pizza(size, *toppings):
    print(f"Making {size.title()}-size pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping.title()}")

make_pizza('small', 'ham','pepper','cheese')
make_pizza('Large', 'tomato','beef')
