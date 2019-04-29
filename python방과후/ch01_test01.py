Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> print("안녕하세요?")
안녕하세요?
>>> print("programmng에 입문하신것을 축하드립니다.")
programmng에 입문하신것을 축하드립니다.
>>> print("programmng에 입문하신 것을 축하드립니다.")
programmng에 입문하신 것을 축하드립니다.
>>> print(2+3)
5
>>> print(2-3)
-1
>>> print(2*3)
6
>>> print(2*3)
6
>>> print(2/3)
0.6666666666666666
>>> print(2345*9876-5678)
23153542
>>> print(3.141592*10.0*10.0)
314.1592
>>> print((1/100)*2345)
23.45
>>> print("강아지+고양이")
강아지+고양이
>>> print("강아지","고양이")
강아지 고양이
>>> print("100"+"200")
100200
>>> print(100+200)
300
>>> print(100+200)
300
>>> print("반가워요"*20)
반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요반가워요
>>> //
SyntaxError: invalid syntax
>>> /!
SyntaxError: invalid syntax
>>> import turtle
>>> t = turtle.Pen()
>>> t.forward(100)
>>> t.upward(100)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t.upward(100)
AttributeError: 'Turtle' object has no attribute 'upward'
>>> t.up(100)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t.up(100)
TypeError: penup() takes 1 positional argument but 2 were given
>>> t.backward(100)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> 
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(90)
>>> t.left(60)
>>> t.forward(100)
>>> t.left(60)
>>> t.left(60)
>>> t.forward(100)
>>> t,left(120)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t,left(120)
NameError: name 'left' is not defined
>>> t.left(120)
>>> t.forward(100)
>>> 
