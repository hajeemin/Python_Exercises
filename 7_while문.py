# current_number=0
# while current_number < 10:
#     current_number += 1
#     current_number = current_number % 2 != 0
    
#     print(current_number)

current_number = 0  #처음 시작할 숫자 정의
while current_number < 10: # 10 미만 값을 구할때
    current_number += 1 # 1을 더하는 식이 있어야 숫자가 하나씩 올라가쥬
    if current_number % 2 == 0: # 넘버를 2로 나눴을 때 0이 나오면
        continue # 0이 나오면 컨티뉴! 0이 안나오면 컨티뉴 건너뛰고 밑으로 가 프린트로
    
    print(current_number) # 그래서 여기에 홀수값이 출력되는 것.
    