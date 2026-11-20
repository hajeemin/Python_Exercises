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

# sandwich_orders.extend(['pastrami','pastrami','pastrami'])
# print(sandwich_orders)

# print(f"Sorry, we are out of {'pastrami'}!")

# while 'pastrami' in sandwich_orders: 
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

# for sandwich in sandwich_orders:
#     sandwich_orders.pop() 
#     finished_sandwiches.append(sandwich)
#     print(f"{sandwich} is now finished!")

# print(finished_sandwiches)
# # 왜 여기서 cheese 샌드위치가 출력이 안되는걸까..............


sandwich_orders.extend(['pastrami','pastrami','pastrami'])
print(f"Ordered Sandwich: {sandwich_orders}")

print(f"Sorry, we are out of {'pastrami'}!")

while 'pastrami' in sandwich_orders: 
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders: # sandwich_order리스트에 원소가 있는 동안 계속 반복
    sandwich = sandwich_orders.pop() # sandwich_order리스트에서 뒤에서 하나씩 꺼내서 삭제하며 샌드위치로 이동
    finished_sandwiches.append(sandwich) # sandwich_order 에서 하나씩 빠진 샌드위치를 finished_sandwices 리스트에 추가.
    print(f"{sandwich}' is now ready!")

print(f"\nfinished Sandwich: {finished_sandwiches}")
# 왜 여기서 cheese 샌드위치가 출력이 안되는걸까..............