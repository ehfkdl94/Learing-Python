'''
a = [0, 20, 30, 40, 50, 60, 70, 80, 90]
print(30 in a)
print(100 in a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(100 not in a)
print(30 not in a)

print(43 in (38, 76, 43, 62, 19))

print(1 in range(10))

print('P' in 'Hello, Python')

a = [0, 10, 20, 30]
b = [9, 8, 7, 6, ]
c= a+b
print(c)


print('Hello ' + str(10))
print('Hello ' + str(1.5))

a = [10, 20, 30, 40] * 3
print(a)

print(len(a))

b= (38, 76, 43, 62, 19)
print(len(b))

hello = 'Hello, World!'
print(len(hello))

hello = '안녕하세요'
print(len(hello))

year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[5:8])
print(population[5:8])
'''
'''
x = str(input().split())
y = str(input().split())
z =x[3:len(x)-2:2] + y[2:len(y)-2:2]
print(z)
'''
x = input()
y = input()
print(x[1::2] + y[::2])
