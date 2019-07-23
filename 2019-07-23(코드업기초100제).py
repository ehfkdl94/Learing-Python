'''
x, y = map(int, input().split())

if x==y:
    print(1)
else:
    print(0)


x, y = map(int, input().split())
if x==0 and y==0:
    print(1)
else:
    print(0)

x, y = map(int, input().split())

if x>y:
    print(x)
else:
    print(y)


x, y, z = map(int, input().split())

if x<y and x<z:
    print(x)
elif y<x and y<z:
    print(y)
else:
    print(z)


x, y, z = map(int, input().split())
if x%2==0:
    print(x)
if y%2==0:
    print(y)
if z%2==0:
    print(z)
'''

x, y, z = map(int, input().split())

if x%2==0:
    print('even')
else:
    print('odd')
if y%2==0:
    print('even')
else:
    print('odd')
if z%2==0:
    print('even')
else:
    print('odd')
