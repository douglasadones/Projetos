from turtle import Turtle, Screen

be = Turtle()


def move_forwar():
    be.forward(20)


def move_backward():
    be.backward(20)


def move_right():
    be.right(20)


def move_left():
    be.left(20)


def clean():
    screen.resetscreen()


screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwar)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clean)
screen.exitonclick()
