#공백 지우기
star ="         *           "
print(star.rstrip())
print(star)
print(star.lstrip())

#접두사 지우기
j_address = "http://www.jemimi.com"
print(j_address.removeprefix("http://"))
j_address_01 = j_address.removeprefix("http://")
print(j_address_01)
print(j_address)
