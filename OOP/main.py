from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")

def move_forwards():
    tim.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()