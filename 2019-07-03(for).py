'''
for i in range(100):
    print('Hello, World!')


for i in range(100):
    print('Hello, World!', i)

for i in range(5, 12):
    print('Hello, World!', i)

for i in range(0, 10, 2):
    print('Hello World!', i)

for i in range(10, 0, -1):
    print('Hello World!', i)

for i in reversed(range(10)):
    print('Hello, world!', i)

for i in range(10):
    print(i, end=' ')
    i=10

count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world!', i)

a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end=' ')

for letter in reversed('Python'):
    print(letter, end=' ')

x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10, end=' ')
'''
x = int(input())

for i in range(1, 10):
    print(x, '*', i, '=', i*x)
