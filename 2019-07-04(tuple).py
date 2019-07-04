'''
a = (38, 21 ,23, 25, 85, 38)
print(a.index(23))
print(a.count(38))

for i in a:
    print(i, end=' ')

a = tuple(i for i in range(10) if i%2==0)
print(a)

a = (1.2, 2.5, 3.6, 4.6)
a = tuple(map(int, a))
print(a)

a=(23, 14, 82,3,48)
print(max(a))
print(min(a))
print(sum(a))

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i)==5]
print(b)

x, y = map(int, input().split())


a=[2**i for i in range(x, y+1)]
a.pop(1)
a.pop(-2)
print(a)
'''

x, y = map(int, input().split())
a = []
for i in range(x, y+1):
    a.append(2**i)
a.pop(1)
a.pop(-2)
print(a)
