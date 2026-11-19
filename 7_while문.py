prompt = '\n원하는 피자 토핑을 입력하세요'
prompt += '\n(더이상 없다면 "종료"를 입력해주세요.):'

topping_2 = [] 
while True:
    topping = input(prompt) #토핑 변수를 만듦
    if topping == "종료": # 종료가 나오면 
        print("\n피자 토핑 추가가 종료되었습니다!") #이렇게 출력됨과 동시에
        break # 루프 멈춤
    else: #종료가 아닐 경우,
        topping_2.append(topping) #토핑 변수에 들어가는 값을 topping_2 리스트에 넣으면서 
        print(f"\n 피자 토핑에 *{topping}* 이 추가되었습니다.") #인풋값을 다시 확인시켜주는 출력을 함

print (f"\n\t*{','.join(topping_2)}* 추가된 피자가 준비되고 있습니다.") # 종료가 되면 topping_2 리스트에 저장해놨던 
                                                                    #값들이 모두 출력되도록!

                                                                    #꺄울 재밋다 
