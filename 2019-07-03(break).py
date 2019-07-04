'''
i = 0
while True:
    print(i)
    i += 1
    if i == 100:
        break

for i in range(10000):
    print(i)
    if i ==100:
        break

for i in range(100):
    if i%2 ==0:
        continue
    print(i)

i =0
while i<100:
    i += 1
    if i%2==0:
        continue
    print(i)

count = int(input('반복할 횟수를 입력하세요: '))

i=0
while True:
    print(i)
    i += 1
    if i==count:
        break

count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count+1):
    if i%2==0:
        continue
    print(i)

i=0
while True:
    if i%10 !=3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1

start, stop = map(int, input().split())

i = start

while True:
    if i%10==3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end=' ')
    i += 1
'''

for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')

    print()

for i in range(5):
    for j in range(5):
        if j==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

for i in range(5):
    for j in range(5):
        if j<i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

x = int(input())
for i in range(x):
    for j in range(x):
        if j <= i:
            print('*', end='')
        else:

            print(' ', end='')
    print()
