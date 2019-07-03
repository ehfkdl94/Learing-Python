'''
x = 10

if x == 10:
    print("10입니다.")

y = 20
if y ==20:
    pass

x = 10
if x==10:
    print("10입니다.")
print("10입니다.")

z = 5
if z ==10:
    print("z에 들어있는 숫자는")
print("10입니다.")

x = 15

if x >= 10:
    print("10이상입니다.")

    if x ==15:
        print("15입니다.")
    if x == 20:
        print("20입니다.")

x = int(input())
if x == 10:
    print("10입니다.")
if x == 20:
    print("20입니다.")

price = int(input())
coupon = input()
if coupon == 'Cash3000':
    price -= 3000
    print(price)
if coupon == 'Cash5000':
    price -= 5000
    print(price)


x = 5
if x == 10:
    print("10입니다.")
else:
    print("10이 아닙니다.")

x=5
if x==10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')

if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')

if 0:
    print('참')
else:
    print('거짓')

if 1:
    print('참')
else:
    print('거짓')

if 0x1F:
    print('참')
else:
    print('거짓')

if 0b1000:
    print('참')
else:
    print('거짓')

if 13.5:
    print('참')
else:
    print('거짓')

if 'Hello':
    print('참')
else:
    print('거짓')

if '':
    print('참')
else:
    print('거짓')

if not 0:
    print('참')

if not None:
    print('참')

if not '':
    print('참')
'''

x = 10
y = 20

if x==10 and y==20:
    print('참')
else:
    print('거짓')

if x > 0 and x  < 20:
    if x <20:
        print('20보다 작은 양수입니다.')

if x>0 and x<20:
    print('20보다 작은 양수입니다.')

if 0 < x < 20:
    print('20보다 작은 양수입니다')

written_test = 75
coding_test = True

if written_test >= 80 and coding_test ==True:
    print('합격')
else:
    print('불합격')

korean, english, math, science = map(int, input().split())
if 0<=korean <=100 and 0<=english<=100 and 0<=math<=100 and 0<=science<=100:
    avg = (korean+english+math+science)/4
    if avg >=80:
        print('합격')
    else:
        print('불합격')

else:
    print('잘못된 점수')
