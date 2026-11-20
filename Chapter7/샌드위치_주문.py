sandwich_orders = ['tuna sandwich', 'ham sandwich','chese sandwich']
finished_sandwiches = []

# while sandwich_orders :
#     for sandwich in sandwich_orders:
#         print(f"{sandwich} is ready!")
#         finished_sandwiches.append(sandwich)

# print(finished_sandwiches) 


while sandwich_orders :
    sandwich = sandwich_orders.pop()
    print(f"{sandwich} is ready!")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches) 