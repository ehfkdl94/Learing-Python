print('Hello, world!'.replace('world', 'Python'))

s = 'Hello, world!'
s = s.replace('world', 'Python')
print(s)

table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

print('apple pear grape pineapple orange'.split())

print('apple, pear, grape, pineapple, orange'.split(', '))
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'ornage']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('PYTHON'.lower())
print('     Python      '.lstrip())
print('     Python      '.rstrip())
print('     Python      '.strip())
print(', python.'.lstrip(',.'))
print(', python.'.rstrip(',.'))
print(', python.'.strip(',.'))

import string
print(', python1.'.strip(string.punctuation))

print(string.punctuation)

print(', python.'.strip(string.punctuation +' '))

print(', python.'.strip(string.punctuation).strip())

print('python'.ljust(10))
print('python'.rjust(10))

print('python'.center(10))
print('python'.rjust(10).upper())

print('35'.zfill(4))
print('3.6'.zfill(6))
print('hello'.zfill(10))

print('apple pineapple'.find('pl'))
print('apple pineapple'.find('le'))
print('apple pineapple'.find('xy'))

print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))

print('apple pineapple'.index('pl'))
print('apple pineapple'.count('pl'))
print('apple pineapple'.count('p'))

name = 'maria'
print('I am %s.' % name)

print('I am %d years old.'%20)
print('%f'%2.3)
print('%.2f'%2.3)
print('%.3f'%2.3)

print('%10s'%'python')
print('%10.2f'%2.3)
print('%10.2f'%2000.3)
print('%-10s'%'python')
print('Today is %d %s.'% (3, 'April'))

print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))

print("Hello, {0} {2} {1}".format('python', 'Script', 3.6))
print("Hello, {2} {1} {0}".format('python', 'Script', 3.6))
print("Hello, {2} {2} {2}".format('python', 'Script', 3.6))
print('{0} {0} {1} {1}'.format('Python', 'Script'))
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))
print('Hello, {language} {version}'.format(language='Python', version=3.6))
language='Python'
version=3.6
print(f'hello, {language} {version}')
print('{{{0}}}'.format('Python'))
print('{0:>10}'.format('python'))

print('%03d'%1)
print('{0:03d}'.format(35))
print('%08.2f'%3.6)

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename=x[-1]
print(filename)

x=path.split('\\')
x.reverse()
filename=x[0]
print(filename)
