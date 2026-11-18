# prompt = '안녕하세요, 반갑습니다.'
# prompt += '\n당신의 이름은 무엇입니까?'

# name = input(prompt)
# print(f"\n반갑습니다, {name}님!")

prompt = '숫자를 입력해보세요!'
prompt += '\n제가 홀수인지 짝수인지 맞춰볼게요!' 
prompt += '\n숫자입력:'


number = int(input(prompt))
if number % 2 == 0:
    print(f"\n{number}... 짝수입니다!")
else:
    print(f"\n{number}... 홀수입니다!")
