import turtle
t = turtle.Turtle()
t.shape("turtle")

# 라스트를 사용하여 색상을 문자열로 저장한다.
color_list = ["yellow","red","blue","green"]

t.fillcolor(color_list[0]) # 채우기 색상을 설정한다.
t.begin_fill() # 채우기를 시작한다.
t.circle(100) # 속이 채워진 원이 그려진다.
t.end_fill() # 채우기를 종료한다.

t.forward(50)
t.fillcolor(color_list[1]) # 채우기 색상을 설정한다.
t.begin_fill()
t.circle(100)
t.end_fill()
turtle.exitonclick()