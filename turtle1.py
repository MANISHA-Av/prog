Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> p=turtle.Pen()
>>> p.speed(0)
>>> p.backward(250)
>>> p.down()
>>> p.color("red", "yellow")
>>> p.begin_fill()
>>> for var in range(300):
	p.forward(500)
	p.left(171)

	
p.en
>>> p.end_fill()
>>> turtle.exitonclick()
