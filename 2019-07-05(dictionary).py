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
