# if-elif-else 예제

age= int(input("How old are you? Insert your age:"))

if age < 4:
    print("No need to buy a ticket. For you it's free!!")
elif 4<= age <18:
    print("Ticket costs 25 dollars each.")
else:
    print("Ticket costs 40 dollars each.")

# print 를 한번만 쓰는 방법이 있음 ⬇️

age= int(input("How old are you? Insert your age:"))
if age < 4:
    price = 0
elif 4<= age < 20:          #이렇게도 할 수 있다니!!! 충격
    price = 25
elif 60<=age:
    price = 20
else:
    price = 40

print(f"당신의 티켓 가격은 {age} dollars 입니다.")
