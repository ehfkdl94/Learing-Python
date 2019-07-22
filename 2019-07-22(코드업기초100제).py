'''
x = int(input())
print("[", int(x/10000)*10000, "]", sep='')
x = x%10000
print("[", int(x/1000)*1000, "]", sep='')
x = x%1000
print("[", int(x/100)*100, "]", sep='')
x = x%100
print("[", int(x/10)*10, "]", sep='')
x = x%10
print("[", x, "]", sep='')


x, y, z = map(int, input().split(":"))
print(y)

x, y, z = map(int, input().split("."))

print("%02d" % z, "%02d" % y, "%04d" % x, sep='-')


x = input()
print("%d"%x)


x, y = map(int, input().split())

print(x+y)

x = int(input())
print(-x)

x, y = map(int, input().split())
print(int(x/y))

x, y = map(int, input().split())
print(int(x%y))


x, y = map(int, input().split())
print(x+y)
print(x-y)
print(x*y)
print(int(x/y))
print(int(x%y))
print("%0.2f"%(x/y))


x, y, z = map(int, input().split())
print(x+y+z)
print("%0.1f"%((x+y+z)/3))

x = int(input())
print(x*2)

import math
x, y = map(int, input().split())
print(2**y)

a, b = map(int, input().split())
if a>b:
    print(1)
else:
    print(0)


a, b = map(int, input().split())
if a==b:
    print(1)
else:
    print(0)


a, b = map(int, input().split())
if a is b:
    print(0)
else:
    print(1)

x = int(input())
if x==1:
    print(0)
else:
    print(1)


x, y = map(int, input().split())
if x==1 and y==1:
    print(1)
else:
    print(0)

x, y = map(int, input().split())
if x==1 or y==1:
    print(1)
else:
    print(0)
'''
x, y = map(int, input().split())
if x==y:
    print(0)
else:
    print(1)
