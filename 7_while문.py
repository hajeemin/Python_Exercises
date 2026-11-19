prompt = '\n좋아하는 도시를 입력해주세요!'
prompt += '\n종료하고싶으면 "quit"을 입력하세요!'


message = ""
while True:
    message = input(prompt)
    if message != 'quit':
       print(f"\n\n저도 {message} 좋아해요!")
    if message == 'quit':
      break 

message = ""
while True:
    message = input(prompt)
    if message == 'quit':
       break
    else:
       print(f"\n\n저도 {message} 좋아해요!")
       
