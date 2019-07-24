'''
x = {'a': 10, 'b': 20, 'c': 30, 'd':40}
x.setdefault('e')
print(x)
x.setdefault('f', 100)
print(x)

x.update(a=90)
print(x)
x.update(e=50)
print(x)

x.update(a=900, f=60)
print(x)

y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)
y.update(zip([1, 2], ['one', 'two']))
print(y)
y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)
y.update({1: 'ONE'})
print(y)

x= {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.pop('a'))
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.popitem())
print(x)

x = {'a':10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)

x={'a':10, 'b':20, 'c': 30, 'd': 40}
print(x.get('a', 0))

print(x.items())
print(x.keys())
print(x.values())

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys, 100)
print(y)

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
print(x['a'])

from collections import defaultdict
y = defaultdict(int)
print(y['z'])

z = defaultdict(lambda: 'python')
print(z['a'])
print(z[0])
print(z)

keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

keys = ['a', 'b', 'c', 'd']
y = {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
print(y)

z = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}
print(z)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

x = {key: value for key, value in x.items() if value != 20}

print(x)

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'oribital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius'])

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
print(x is y)

y['a'] = 99
print(x)
print(y)



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
'''
