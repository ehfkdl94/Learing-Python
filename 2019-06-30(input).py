x = 10
print(x)
y = 'Hello, World!'
print(y)

print(type(x))
print(type(y))

x, y, z = 10, 20, 30
print(x, y, z)

a = b = c = 10
print(a, b, c)

x, y = 10, 20
x, y = y, x

print(x, y)

x = None
print(x)

a, b = 10, 20
c = a+b
print(c)

a=10
a = a+20
print(a)

b +=20
print(b)

x = -10
print(+x)
print(-x)

#a = input()
#print(a)

#a = input('첫 번째 숫자를 입력하세요:')
#b = input('두 번째 숫자를 입력하세요:')
#print(a+b)

#a = int(input('첫 번째 숫자를 입력하세요:'))
#b = int(input('두 번째 숫자를 입력하세요:'))
#print(a+b)

#a = float(input("첫 번째 실수를 입력하세요:"))
#b = float(input("두 번째 실수를 입력하세요:"))
#print(a+b)

#a, b = input("문자열 두 개를 입력하세요:").split()
#print(a, b)

#a, b = input('숫자 두 개를 입력하세요:').split()
#a = int(a)
#b = int(b)
#print(a+b)

#a, b = map(int, input('숫자 두 개를 입력하세요').split())
#print(a+b)

a, b = map(int, input('숫자 두 개를 입력하세여:').split(','))
print(a+b)
