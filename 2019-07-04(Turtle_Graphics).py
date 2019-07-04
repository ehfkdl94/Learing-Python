'''
import turtle as t
t.shape('turtle')
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)


import turtle as t

t.shape('turtle')

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.mainloop()


import turtle as t

t.shape('turtle')

for i in range(4):
    t.fd(100)
    t.rt(90)

import turtle as t
t.shape('turtle')
for i in range(5):
    t.fd(100)
    t.rt(360/5)
t.mainloop()


import turtle as t

n = int(input())
t.shape('turtle')
t.color('#FF69B4')
t.begin_fill()
for i in range(n):
    t.fd(100)
    t.rt(360/n)
t.end_fill()
t.mainloop()


import turtle as t
t.shape('turtle')
t.color('#FF69B4')
t.begin_fill()
t.circle(120)
t.end_fill()


import turtle as t

n=60
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.circle(120)
    t.right(360/n)


import turtle as t

t.shape('turtle')
t.speed('fastest')
for i in range(300):
    t.fd(i)
    t.rt(91)


import turtle as t

n=5
t.shape('turtle')
for i in range(n):
    t.fd(100)
    t.rt(144)
    t.fd(100)
    t.lt(72)


import turtle as t
n=5
t.shape('turtle')
for i in range(n):
    t.fd(100)
    t.rt((360/n)*2)
    t.fd(100)
    t.lt(360/n)
'''
import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.fd(line)
    t.rt((360/n)*2)
    t.fd(line)
    t.lt(360/n)
t.mainloop()
