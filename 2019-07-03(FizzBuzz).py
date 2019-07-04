'''
for i in range(1, 101):
    if i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)

for i in range(1, 101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
for i in range(1, 101):
    if i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0 and i%5==0:
        print('FizzBuzz')
    else:
        print(i)
for i in range(1, 101):
    if i%15 ==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

for i in range(1, 101):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0)or i)

for i in range(1, 101):
    if i%2==0 and i%11==0:
        print("FizzBuzz")
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)
'''
x, y = map(int, input().split())
for i in range(x, y+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)
