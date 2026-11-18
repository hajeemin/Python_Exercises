# 외계인 30명 만들기

aliens = [] # 우선 빈 외계인 리스트를 만들기 
for alien_number in range(30): # range()함수는 숫자를 반환하고 파이썬은 이 숫자만큼 루프반복
    new_alien = {'color':'green', 'points':5, 'speed':'slow'} # 루프 진행하면서 새외계인을 만듦
    aliens.append(new_alien) # new_alien을 aliens 리스트에 추가.

for alien in aliens[:5]: # 지금 aliens 리스트에 30명의 외계인이 저장되어있음. 
    print(alien)        #여기서 alien으로 aliens안의 원소들을 하나씩 빼며 프린트.
print("...")

print(f"Total number of aliens:{len(aliens)}")

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

print(aliens)

