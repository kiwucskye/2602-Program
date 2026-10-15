t = int(input('근무시간을 입력하세요. '))
a = 24
c = a // t
addc = 1 if ( a % t ) > 0 else 0
print('필요한 컴퓨터 : ', c + addc)
