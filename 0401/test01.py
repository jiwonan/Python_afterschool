import turtle
t = turtle.Turtle()
t.shape("turtle")
#size = int(input("집의 크기는 얼마로 할까요? ")) #100입력
size = int(turtle.textinput("", " 집의 크기는 얼마로 할까요? "))
t.forward(size) # size 만큼 거북이를 전진시킨다.
t.right(90) # 거북이를 오른쪽으로 90도 회전시킨다.
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
# 거북이를 오른쪽으로 90도 회전시켜서 오른쪽을 보도록 한다.
t.right(90)
# 지붕을 그리면 된다.
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
turtle.exitonclick()