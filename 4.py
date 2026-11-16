# 4-10 연습문제

my_foods = ['pizza','burger','chicken','beef','ramen']
print(f"리스트의 첫 세 항목은:\n{my_foods[:3]}")
print(f"리스트의 중간 세 항목은:\n{my_foods[1:4]}")
print(f"리스트의 마지막 세 항목은:\n{my_foods[-3:]}")

#4-11

my_pizzas = ['pepperoni','diavolo','margeritta']
friends_pizzas = my_pizzas[:] # 공유가 아니라 복사임!!! 친구가 내 피자 복사한거임!! 서로 별개!!

my_pizzas.append('hawaian')
friends_pizzas.append('hot-chicken')

print("my fav pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("my friend's fav pizzas are:")
for pizza in friends_pizzas:
    print(pizza.title())

