sandwich_orders = ['tuna sandwich', 'ham sandwich','cheese sandwich']
finished_sandwiches = []

# while sandwich_orders :
#     for sandwich in sandwich_orders:
#         print(f"{sandwich} is ready!")
#         finished_sandwiches.append(sandwich)

# print(finished_sandwiches) 


# while sandwich_orders :
#     sandwich = sandwich_orders.pop()
#     print(f"{sandwich} is ready!")
#     finished_sandwiches.append(sandwich)

# print(finished_sandwiches) 

sandwich_orders.extend(['pastrami','pastrami','pastrami'])
print(sandwich_orders)

print(f"Sorry, we are out of {'pastrami'}!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

for sandwich in sandwich_orders:
    sandwich_orders.pop() 
    finished_sandwiches.append(sandwich)
    print(f"{sandwich} is now finished!")

print(finished_sandwiches)
# 왜 여기서 cheese 샌드위치가 출력이 안되는걸까..............