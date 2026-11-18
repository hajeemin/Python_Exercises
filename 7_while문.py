# # # prompt = '안녕하세요, 반갑습니다.'
# # # prompt += '\n당신의 이름은 무엇입니까?'

# # # name = input(prompt)
# # # print(f"\n반갑습니다, {name}님!")

# # prompt = '숫자를 입력해보세요!'
# # prompt += '\n제가 홀수인지 짝수인지 맞춰볼게요!' 
# # prompt += '\n숫자입력:'


# # number = int(input(prompt))
# # if number % 2 == 0:
# #     print(f"\n{number}... 짝수입니다!")
# # else:
# #     print(f"\n{number}... 홀수입니다!")

# prompt = '\n안녕하세요!'
# prompt +='\n초파 렌터카 입니다!'
# prompt +='\n어떤 차를 원하시나요?'

# car = input(prompt)
# print(f"\n잠시만 기다려주세요! {car}! 준비되고 있습니다!")

number_people = int(input("오늘 식사자리에 몇 명이 참석하나요?"))
if number_people >= 9:
    print(f"대기가 필요합니다.")
if number_people <= 8:
    print(f"\n 홀 안으로 입장해 주세요!")