# list = [1:10]
# print(list) #ㅋㅋ..

numbers = list(range(1,10))
print(numbers)

for number in numbers:
    if number == 1:
        print(number,'st')
    elif number == 2:
        print(number,'nd')
    elif number == 3:
        print(number,'rd')
    else:
        print(number,'th')

#루프 안에서 if-elif-else 문을 사용해 각 숫자에 맞는 서수 접미사를 출력하세요. 이들은 별도 행으로 출력되어야합니다. 

numbers = list(range(1,10))
print(numbers)

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")