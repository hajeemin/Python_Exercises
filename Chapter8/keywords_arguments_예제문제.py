def sandwich_orders(*sandwiches_ingredients):
    print("Making sandwich with the following ingredients:")
    for ingredient in sandwiches_ingredients:
        print(f"-{ingredient}")

sandwich_orders('tuna')
sandwich_orders('ham','cheese')
sandwich_orders('avocado','shrimp','lettuce')

