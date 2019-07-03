'''
i = 0
while i < 100:
    print('Hello, World!')
    i += 1

i = 1
while i <=100:
    print('Hello, world!', i)
    i += 1

i = 100
while i > 0:
    print('Hello, world!', i)
    i -= 1

count = int(input('반복할 횟수를 입력하세요:'))

i = 0
while i < count:
    print('Hello, world!', i)
    i += 1

count = int(input('반복할 횟수를 입력하세요: '))

while count > 0:
    print('Hello, World!', count)
    count -= 1
'''
import random
print(random.random())

print(random.randint(1, 6))
print(random.randint(1, 6))

i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)

dice = [10, 20, 30, 40, 50, 60]
print(random.choice(dice))
print(random.choice(dice))
print(random.choice(dice))

i = 2
j = 5

while i <= 32 or j >=1:
    print(i, j)
    i *= 2
    j -= 1

x = int(input())

while x >=1350:
    x -= 1350
    print(x)
