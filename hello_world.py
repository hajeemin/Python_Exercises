#print("Hello, World!")

def greeting():
    hi = int(input("안녕하세요? 반갑습니다. 당신도 반가우면 숫자 0~10까지 눌러주세요."))
    if hi ==7: print("앗 당신도 제가 반가우시군요!!행복합니당")
    elif 0<= hi <=6: print("아직 제가 덜 반가우시군요!! 다시 숫자를 눌러주세요.")
    elif 8<= hi <=10: print("너무 과하네여! 다시 숫자를 눌러주세요.") 


greeting()

