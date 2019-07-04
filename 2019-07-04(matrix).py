a = [[10, 20],
     [30, 40],
     [50, 60]]
print(a)
print(a[0][0])
print(a[1][1])
print(a[2][1])
a[0][1] = 1000
print(a)

a=[]
a.append([])
a[0].append(10)
a[0].append(20)
print(a)
a.append([])
a[1].append(500)
a[1].append(600)
a[1].append(700)
print(a)

from pprint import pprint
a=[[10,20], [30, 40], [50, 60]]
pprint(a, indent=2, width=20)


a=[[10,20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y)

a=[[10,20], [30, 40], [50, 60]]

for i in a:
    for j in i:
        print(j ,end=' ')
    print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

print(a[0])
print(a[1])
print(a[2])
print(len(a[0]))

a=[[10,20], [30, 40], [50, 60]]

i =0
while i<len(a):
    x, y = a[i]
    print(x, y)
    i += 1


a=[[10,20], [30, 40], [50, 60]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1


a=[]
for i in range(10):
    a.append(0)

print(a)

a = []
for i in range(3):
    line=[]
    for j in range(2):
        line.append(0)
    a.append(line)
pprint(a, indent=4, width=20)

a = [[0 for j in range(2)] for i in range(3)]
print(a)

a = [[0]*2 for i in range(3)]
print(a)

a = [3, 1, 3, 2, 5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

a = [[0]* i for i in [3, 1, 3, 2, 5]]
print(a)

students = [
    ['join', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
print(sorted(students, key=lambda student: student[1]))

print(sorted(students, key=lambda student: student[2]))

a = [[10, 20], [30, 40]]
b=a
b[0][0] = 500
print(a)
print(b)

a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)

import copy
a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)
b[0][0] = 500
print(a)
print(b)

a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(a)
pprint(a, indent=2, width=40)
