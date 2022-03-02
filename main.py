import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=760, height=520)

guess = screen.textinput(title="Guess the State", prompt="What's another state's name?")

# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()


# screen.exitonclick()
