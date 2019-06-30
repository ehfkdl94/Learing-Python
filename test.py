#a=int(input())
#b=int(input())
#print(a+b)

#a = input().split(', ')
#print(a)

#map(함수, 대상자료)
#a, b, c = map(int, input().split(' '))
#print(a+b+c)

#a=9.1
#print(a, "을 반올림하면", 9, '입니다.', sep='') #sep=''띄워쓰기부분에 원하는 값을 넣을 수 있음
#print("ㅇㅇㅇ", end='')#end=''넣으면 줄바꿈 안됨

#a=2>1
#print(a)

#a = 2==2
#print(a)


#==은 오로지 값만 가지고 비교 is는 내부적으로 다른것까지 비교
# 2 == 2.0 (true), 2 is 2.0 (false)

#a = 2 is 2.0
#print(a)

#a = 2 != 2.0
#print(a) #false

#a= 2 is not 2.0
#print(a) #true

#a = not False #and,  or, not
#print(a)
#0, 0.0, '', "", None 5가지는 거짓

#a= 'B' and True
#print(a)
'''
a, b, c, d, e = map(int, input().split(', '))
avg = int((a+b+c+d+e)/5)
a1 = a>=40 and b>=40 and c>=40 and d>=40 and e>=40 and avg>=60


print("평점 ", avg, "점", a1, "입니다.", sep='')
'''

'''
h="hi"
t="python!"
print(len(h+t))
'''

'''
h="hi"
t="python!"
h += t

print(h[:5]) #2에서 끝까지 [2:] 또는 [2:len(h)]
'''

#시퀀스(연속적) 자료형 - list, tuple, range, str, bytes, bytearray
#리스트 :c에서 연결리스트라고 생각하면됨
#range(시작, 끝)
#a=[1, 2.0 , "문자열", ["다른 리스트", 1]]
#c=list(range(0,10,2))
#b=list(range(10, 0, -2))
#print(b)
#print(c)

#tuple
#a=(1,2,3)#tuple은 읽기전요 추가, 변경이 안됨
#b=1, #(1,)
#c=("어떤거든", 123, 1.3)
#d=tuple(range(1,11))
#print(d)

#언팩킹
#a,b,c = [1,2,3] # =  a,b,c = (1,2,3) 같다
#d,e,f = ('123')
#g=list("문자열")
#print(a,b,c)
#print(d,e,f)
#print(g)

#값 in 시퀀스자료형
#a=[0,1,2,3]
#b=2 in a # 시퀀스 안에 2가 있는지 없는지 true false로 나옴
#c=5 not in a #시퀀스 안에 5가 없으면 true
#d=[3,4,5]
#f="안녕?"
#print(len(f.encode('utf-8')))
#del a[1]
#print(a)

#a=[1,2,3,4,5,6,7]
#print(a[1:3])
#a[1:3] = [10,11,12]
#print(a)
#del a[1:4]
#print(a)

#a = list(range(7,101,7))
#a += [777]
#print(a)

#딕셔너리 (순서가없다.)
#dict = {키:값, 키:값}

#d1 = {}
#d2 = dict()
#print(d1,d2)

#다리우스 = {'HP':1000, 'MP':500, '공격력':200, '방어력':50}
#다리우스['방어력'] = 100
#print(다리우스)
#del 다리우스['방어력']
#print(다리우스)
#다리우스['방어력'] = 100
#print(다리우스)
#print(len(다리우스))
#a = 100 in 다리우스
#print(a)
#b = 다리우스.keys()
#c = 다리우스.values()
#print(b)
#print(c)

#if 조건문:
    #코드

#x = 10
#if x<5:
#    print(x)
#elif x==5:
#    print('x>5')
#else:
#    print('else')

#for i in list(range(5)):
#    print(i)

#for i in reversed('abcde'):
#    print(i)

#구구단
'''
x = int(input('입력 : '))
if x<1 or x>9:
    print("1~9사이의 숫자가 아닙니다.")
else:
    print('출력 : ')
    if x%2==0:
        for i in range(2,10,2):
            print(x,'*',i,'=',x*i, sep='')
    else:
        for i in range(1,10,2):
            print(x,'*',i,'=',x*i, sep='')
'''

#while 조건문:
#    실행할코드
#i=10
#while i>0:
#    print('hi', i)
#    i-=1

#교통비 1350원, 교통카드=10000원
#사용할떄마다 남은 잔액을 계속 출력, 사용불가능하면 잔액이 부족합니다를 출력
'''
card = int(10000)

while card > 1350:
        card -= 1350
        print('잔액은',card, "원")
print("잔액이 부족합니다.")
'''




#별만들기랑 터틀
'''
import turtle as t
t.shape('turtle')
t.color('black')
t.begin_fill()
n=5
for i in range(n):
    t.forward(100)
    t.right((360/n)*2)
    t.forward(100)
    t.left(360/n)
t.end_fill()
t.speed('fastest')
t.right(135)
t.forward(n*10)
t.left(135)
for j in range(320):
    t.forward(j)
    t.right(91)
input()
'''
'''
for i in (1,3):
    for j in range(1,3):
        print(' ', end='')
    for k in range(1,8,2):
        print('*')
'''

'''
   *
  ***
*******
  ***
   *

j=int(1)
for i in range(4,0,-1):
    if j==5:
        j+=2
        continue
    print(' '*(i-1), '*'*j)
    if j==7:
        break
    j+=2
j=5
for i in range(1,4):
    if j==5:
        j-=2
        continue
    print(' '*i, '*'*j)
    j-=2
'''

#a = [1,2,3,4,5]
#a.insert(2, 6) # 2번쨰 자리에 6을 넣는다
#print(a)

#a = list(range(1,11))
#a.append(100) #마지막에 100을 추가
#print(a)

#a = list(range(1,11))
#b=[20,30]
#a.extend(b)
#print(a)

#a = list(range(1,11))
#b=a.pop() #맨마지막 요소를 뽑아내고 리스트에서 삭제시킴
#print(b)
#print(a)

#a=list(range(1,11))
#a.remove(5) #리스트에서 5인 값을 지우고싶을때
#print(a)

#a=list(range(1,11))
#b = a.index(2) # 2가 인덱스를 반환
#print(a)
#print(b)

#a = list(range(1,11))
#a +=[1]
#b=a.count(1) #똑같은 요소가 몇개있는지 알려줌
#print(b)
#print(a)

#a = list(range(1,11))
#a.reverse() #리스트를 뒤집는다
#print(a)

#a = list(range(1,11))
#a[4] =10
#a[9]=5
#a.sort(reverse=True) #a.sort()오름차순으로 소팅, a.sort(reverse=True) 내림차순
#print(a)

#a = list(range(1,11))
#a[4]=10
#a[9]=5
#b = sorted(a) #a.sort는 a를 정렬하는데 sorted는 a자체를 정렬하는게 아니라
               #a를 불러와서 정렬하고 b에 저장한다 a는 그대로유지
#print(a)
#print(b)

#a = list(range(1,11))
#a.clear() # 리스트를 초기화
#print(a)

#a = list(range(1,11))
#b=a.copy() #b=a넣으면 값을 복사하는게 아니라 참조하는것이라서 인덱스 값을 변경해줘도
            #변하지 않는데 copy를 해줘야지 값이 복사가됨
#a[0]=99
#print(a,b)

#a = list(range(1,11))
#print(min(a)) #리스트에서 가장작은값을 반환 max(a)가장 큰값
#print(sum(a)) #리스트요소들의 합출

#a=list(range(1, 11))
#for index, value in enumerate(a, start=10):
#    print(index, value)

#[식 for 변수 in 반복가능한객체]
#a=[i for i in range(11, 21) if i%2==1] #i를 값을 넣고  조건문에 만족하면 식을 실행
#print(a)

#a=[i for i in range(11,21) if i%2==1 if i>15]
#print(a)

#a=[i*j for i in range(2,10) for j in range(1,10) if i%2==0 if j%2==0]
#print(a)

#a=list(map(함수, 리스트))

#a=list(range(10))
#b=list(map(str, a))
#print(b)

#a=tuple(range(10))
#b=tuple(map(str,a))
#print(b)

#a=tuple(range(10))
#b=list(map(str,a))
#print(b)

#a=tuple(i*2 for i in range(10) if i*2<10)
#print(a)

#print([i for i in range(3)])

#a = [[1,2], [3], [4,5,6]]
#print(a[0][0])

#b = []
#for i in range(3):
#    nw=[]
#    for j in range(3):
#        nw.append(j)
#    b.append(nw)
#
#print(b)

#b = [[0 for j in range(2)] for i in range(3)]
#print(b)

#b =[[0]*2]
#print(b)

#b = [[0 for j in range(2)] *2]
#print(b)

#c = [[i]*i for i in [3,1,5]]
#print(c)

#b = [[1,2], [3,4], [5,6]]
#for x,y in b:
#    print(x,y)

#b = [[1,2], [3,4], [5,6]]
#for i in range(len(b)):
#    for j in range(len(b[i])):
#        b[i][j] = i*j
#
#print(b)

#import copy
#a = [[1], [2,3]]
#b = copy.deepcopy(a)
#b[0][0] = 5

#print(a)
#print(b)

#a = "Hi, I am python"
#print(a.upper()) #대문자로 변경
#print(a)
#a=a.upper()
#print(a)
#print(a.lower()) #소문자로 변경

#a = " Hi, I am python"
#print(a.find('Hi'))

#a = "am"
#b = 4.5
#print("I %-10s python, %f"%(a,b))

#a = "I am {0}".format("apple")
#b=13
#c=1.3
#print('I am {2} {1} {0}'.format('python', b, c))

#a = "{V}".format(V=13)
#print(a)

#d = {'a':1, 'b':2, 'c':3}
#d.update(d=4)
#print(d)
#print(d.pop('b'))
#print(d)
#for k,v in d.items():
#    print(k,v)

#b = {key:value for key, value in d.items() if value%2==0}
#print(b)

#import copy
#dd = {'a':{'A':1}, 'b':{'B':2}}
#print(dd['a']['A'])
#x =copy.deepcopy(dd)
#dd['b']['B']=3
#print(dd)

#fruits = {'a', 'b', 'c', 'd', 'e'}
#print(fruits)

'''
a = {1,2,3,4}
b = {3,4,5,6}
c=a|b
d=a&b
e=a-b
f=a^b
a |=b
a.add(7)
a.remove(1)
print(c)
print(d)
print(e)
print(f)
print(a)
print(a.len())
'''

#s = set()
#e = {i for i in 'pineapple' if i not in 'apl'}
#print(e)

#file = open('hi.txt', 'w+')
#file.write("문자열들")
#file.close()
#file2 = open('hi.txt', 'r')
#a = file2.read()
#print(a)
#file2.close()
#with open("hi2.txt", "w+") as f:
#    f.write("새로운 문자열")

#li = ["문자열1", "문자열2", "문자열3"]
#with open('hi.txt', 'a+') as f:
#    for i in li:
#        f.write('\n나는 %s'%i)

#def cul(a,b):
#    print(a,b)
#    return a+b

#print(cul(b=2,a=3))

#def hi(i):
#    if i<=0:
#        return
#    print("hi {0}".format(i))
#    i-=1
#    hi(i)
#hi(5)

#j = lambda x:x**x
#j = (lambda x:x**x)(10)

#def z(x):
#    return x**x

#print((lambda x:x**x)(10))
#print(z(10))
#
#j=list(map(lambda x, y:x*y, [2,3,4], [6,7,8]))
#print(j)

#a=[1,2.0,3,4.1,5]
#c = list(map(lambda x:True if type(x)==int else False, a))
#print(c)

#x=10
#def f1():
#    x=20
#    print(locals())
#    print(x)
#
#f1()
#print(x)
#print(locals())
#if __name__ == "__main__":
#    print('시작')

#y = 10
#print(y)
#def f1():
#    global y
#    y=20
#    x=1
#    def f2():
#        nonlocal x
#        y=30
#        x=5
#        print(y,x)
#        def f3():
#            nonlocal x
#            x=10
#            print(y,x)
#        f3()
#    f2()
#    print(y,x)
#f1()
#print(y)

#클로저
#def cal():
#    a,b = 5,7
#    def ma(x):
#        return a*x+b
#    return ma
#c = cal()
#print(c)
#print(c(1), c(2), c(3))
#
#def cal1():
#    a,b=5,7
#    return lambda x:a*x+b
#c=cal1()
#print(c(4), c(5))

#a = list(range(1,11))
#def f1():
#    def f2(x):
#        for i in x:
#            if i%2==1:
#                print(i*10)
#            else:
#                print('False')
#    return f2
#c = f1()
#c(a)

#class Bm:
#    def __init__(self):
#        self.color="검은색"
#    def write(self):
#        print("%s 마커 쓰기"%self.color)
#maker=Bm()
#maker2=Bm()
#maker.write()
#maker2.color="빨간색"
#maker2.write()
#print(maker.color)
#print(maker2.color)

'''
class Bm:
    def __init__(self, color, simji):
        self.__color=color##언더바 2개 붙으면 private
        self.simji=simji##언더바 2개가 안붙으면 public
    def write(self, color):
        self.__color=color
        print(self.simji, "심지의", self.__color, "보드마카")
marker = Bm("검은색", "뾰족한")
marker.write("빨간색")
marker.__color="파란색"
'''

'''
class Bm:
    pass#빈 클래스 작성할때 pass를 넣어줌 함수도 마찬가지
print('a')
'''

'''
class Person:
    __bigbag=[]
    subbag=[]
    def put_bag(self, pencil):
        Person.subbag.append(pencil)
    def move_bag(self):
        Person.__bigbag=Person.subbag.pop()
    def print_bag(self):
        print(Person.__bigbag)
A=Person()
B=Person()
A.put_bag("연필1")
B.put_bag("연필2")
print(Person.subbag)
B.move_bag()
B.move_bag()
print(Person.subbag)
print(A.subbag)
A.print_bag()
'''

'''
class Calc:
    count=0
    def __init__(self):
        Calc.count+=1
    @staticmethod
    def add(a, c):
        print(a+c)
    @staticmethod
    def mul(a,c):
        print(a*c)
    @classmethod
    def print_count(cls):
        print('{0}번 생성됨.'.format(cls.count))
Calc.add(1,2)
Calc.mul(2,3)
a = Calc()
b = Calc()
Calc.print_count()
a.print_count()
'''
'''
class Person:
    def __init__(self):
        print("Person init")
        self.hi="안녕?"

class Student(Person):
    def __init__(self):
        print("Student init")
        super().__init__()
        self.name="파이썬"

B = Student()
print(B.name)
print(B.hi)
'''
'''
class Person:
     def __init__(self):
         print("Person init")
         self.hi="안녕?"
class Student(Person):
    pass
B=Student()
print(B.hi)
'''
'''
class Person:
    def hi(self):
        print("안녕하세요")
class Animal:
    def name(self):
        print("토끼")
class Student(Person, Animal):
    def who(self):
        print("나는 파이썬")
B=Student()
B.hi()
B.name()
B.who()
'''
'''
class A:
    def hi(self):
        print("A입니다.")
class B(A):
    def hi(self):
        print("B입니다.")
class C(A):
    def hi(self):
        print("C입니다.")
class D(C,B):
    pass

d = D()
d.hi()
print(D.mro())#메소드 리솔루션 오더 클랙스탐색순
'''

'''
def deko(fun):
    def w():
        print(fun.__name__, '시작')
        fun()
        print(fun.__name__, '끝')
    return w
@deko
def hi():
    print("hi")
@deko
def app():
    print("app")
hi()
app()
'''
#예외처리
'''
try:
    a=10/int(input())
    print(a)
except:
    print("예외발생", a)
'''

'''
a=[10,20,30]
try:
    index, x = map(int, input().split())
    b=100
    print(a[index]/x)
except Exception as err:
    print(err)
else:
    print("성공")
finally:
    print("프로그램 종료")

print(b)
'''
'''
def three_multiple():
    try:
        x=int(input("3배수 : "))
        if x%3 !=0:
            raise Exception('3의 배수가 아님')
        print(x)
    except Exception as err:
        print("이 함수에서 예외발생", err)
        raise
three_multiple()
'''

#import math as m
#print(m.sqrt(4.0))

#from math import sqrt as s, pi as p
#print(s(4.0), p)
'''
import urllib.request as u
r=u.urlopen('http://www.google.co.kr')
print(r.status)
'''
#PSL(python standard library)

#import t
#print(t.sq(3))

#from calpkg import add1, mul1
#print(add1.myadd(1,2), mul1.mymul(3,4))

class Node:
    def __init__(self, data=None):
        self.data=data
        self.link=None
class linkedlist:
    def __init__(self):
        self.head=Node()
        self.positionnow=self.head
    def InsertNode(self, data):
        newnode=Node(data)
        self.positionnow.link=newnode
        self.positionnow=newnode
    def PrintNode(self):
        print("Data = ", end='')
        self.H=self.head
        while self.H.link != None:
            self.H=self.H.link
            print(self.H.data, end=' ')
        print()
    def DeleteNode(self, data):
        self.pre=self.head
        self.D=self.head.link
        while self.D != None:
            if self.D.data==data:
                break
            self.pre=self.D
            self.D=self.D.link
        if self.D==None:
            print("해당 객체를 찾을 수 없습니다.")
        else:
            self.pre.link = self.D.link
            if self.D.link==None:
                self.prositionnow=self.pre
                del self.D
N=linkedlist()
N.InsertNode("A")
N.InsertNode("C")
N.InsertNode("B")

N.PrintNode()
N.DeleteNode("C")
N.InsertNode("D")
N.PrintNode()
