a = [38, 21, 53, 62, 19]
print(a[0])
print(a[2])
print(a[4])

b = (38, 24, 53, 62, 19)
print(b[0])

r = range(15)
print(r[2])

hello = 'Hello, World!'
print(hello[2])

a = [38, 21, 53, 62, 19]
print(a[-1])
print(a[-5])

b = (38, 21, 53, 62, 19)
print(b[-1])

hello = 'Hello, World!'
print(hello[-4])

a=[0, 0, 0, 0, 0]
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[4] = 19
print(a)

del a[2]
print(a)

a=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:4])

print(a[4:-1])

print(a[2:8:3])
print(a[2:9:3])
print(len(a))
print(a[:10])
print(a[7:])
print(a[:])
print(a[:7:2])
print(a[::2])
print(a[5:1:-1])
print(a[:len(a)])

print(range(10)[slice(4, 7, 2)])

s = slice(4, 7)
print(s)
print(a[s])

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c']
print(a)
a[2:5] = ['x']
print(a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e']
print(a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:8:2] = ['a', 'b', 'c']
print(a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:5]
print(a)
