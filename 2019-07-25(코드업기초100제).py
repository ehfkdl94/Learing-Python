'''
x = int(input())

if x>0:
    print('plus')
    if x%2==0:
        print('even')
    else:
        print('odd')
else:
    print('minus')
    if x%2==1:
        print('odd')
    else:
        print('even')


x = int(input())

if x>=90 and x<=100:
    print('A')
elif x>=70 and x<90:
    print('B')
elif x>=40 and x<70:
    print('C')
elif x>= 0 and x<40:
    print('D')


x = input()

if x =='A':
    print('best!!!')
elif x=='B':
    print('good!!')
elif x=='C':
    print('run!')
elif x=='D':
    print('slowly~')
else:
    print('what?')

x = int(input())

if x==12 or x==1 or x==2:
    print('winter')
elif x ==3 or x==4 or x==5:
    print('spring')
elif x==6 or x==7 or x==8:
    print('summer')
elif x==9 or x==10 or x==11:
    print('fall')

x = int(input())
for i in range(x, 0, -1):
    print(i-1)


x = input()
x = ord(x)
for i in range(97, x+1):
    print(chr(i), end=' ')


x = int(input())
for i in range(0, x+1):
    print(i)


x = int(input())
sum=0
for i in range(0, x+1):
    if i%2==0:
        sum += i
print(sum)


x = int(input())
sum=0
for i in range(1, 1001):
        sum += i
        if sum>=x:
            break
print(i)


x, y = map(int, input().split())
for i in range(1, x+1):
    for j in range(1, y+1):
        print(i, j)


x = int(input())

for i in range(1, x+1):
    if i%3==0:
        print('X', end=' ')
    else:
        print(i, end=' ')
'''

r, g, b = map(int, input().split())
sum = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            sum += 1
print(sum)
