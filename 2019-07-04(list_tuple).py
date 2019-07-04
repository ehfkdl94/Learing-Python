a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

a = []
a.append(10)
print(a)

a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

a=[10, 20, 30]
a.insert(0, 500)
print(a)

a=[10, 20, 30]
a.insert(len(a), 500)
print(a)

a=[10, 20, 30]
a[1:1] = [500, 600]
print(a)

a=[10, 20, 30]
print(a.pop())
print(a)

a=[10, 20, 30]
print(a.pop(1))
print(a)

a=[10, 20, 30]
a.remove(30)
print(a)

a = [10, 20, 30, 20]
a.remove(20)
print(a)

from collections import deque
a = deque([10, 20, 30])
print(a)
a.append(500)
print(a)
print(a.popleft())
print(a)

a = [10, 20, 30, 15, 20, 40]
print(a.index(20))
print(a.count(20))
print(a)
a.reverse()
print(a)

a=[10, 20, 30, 15, 20, 40]
print(a)
a.sort()
print(a)
a.clear()
print(a)

a=[10, 20, 30, 15, 20, 40]
del a[:]
print(a)

a = [10, 20, 30]
a[len(a):] = [500]
print(a)

a = [10, 20, 30]
a[len(a):] = [500, 600]
print(a)
b = []
if not len(b):
    print('리스트가 비어있습니다.')
if len(a):
    print('리스트에 요소가 있습니다.')

if not b:
    print('리스트가 비어있습니다.')
if len(a):
    print('리스트에 요소가 있습니다.')

b = [10, 20, 30, 40]
print(b[-1])

a = [1,2,3,4,5]
b=a
print(a is b)

b[2] = 99
print(a)
print(b)

a = [0,0,0,0,0]
b = a.copy()
print(a is b)
print(a == b)

b.insert(2, 3)
print(a)
print(b)

a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

for index, value in enumerate(a):
    print(index, value)
print()

for index, value in enumerate(a, start=1):
    print(index, value)
print()

for i in range(len(a)):
    print(a[i])
print()
i=0
while i < len(a):
    print(a[i])
    i += 1

i=0
while i <len(a):
    print(i+1, a[i])
    i += 1
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i< smallest:
        smallest = i

print(smallest)

a= [24, 43, 36, 57,34,123,46,7,35,76,44,21]
biggest = a[0]

for i in a:
    if i>biggest:
        biggest=i

print(biggest)

a.sort()
print(a[0])

a.sort(reverse=True)
print(a[0])

print(min(a))
print(max(a))

x=0
for i in a:
    x += i
print(x)

print(sum(a))

a = [i for i in range(10)]
print(a)

b=list(i for i in range(10))
print(b)

c = [i+5 for i in range(10)]
print(c)
d = [i*2 for i in range(10)]
print(d)

a = [i for i in range(10) if i%2==0]
print(a)

b = [i+5 for i in range(10) if i%2==1]
print(b)

a = [i*j for j in range(2, 10)
         for i in range(1, 10)]
print(a)

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

a = map(int, input().split())
print(a)
print(list(a))

a, b = [10, 20]
print(a)
print(b)

x= input().split()
m = map(int, x)
a,b = m
print(a)
print(b)
