import turtle
import pandas


def write_state(name_state, x, y):
    timmy.goto(x=x, y=y)
    timmy.write(f"{name_state}", move=False, font=("Arial", 8, "normal"), align="center")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=760, height=520)

timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")

game_is_running = True
data = pandas.read_csv("50_states.csv")
correct_guesses = []
score = 0

while game_is_running:

    guess = screen.textinput(title=f"{score}/50 States guessed!", prompt="What's another state's name?")

    for state in data.state:
        if guess is None:
            game_is_running = False
        elif guess.title() in correct_guesses:
            pass
        elif guess.title() == state:
            location = data[data.state == guess.title()]
            write_state(name_state=state, x=int(location.x), y=int(location.y))
            correct_guesses.append(state)
            score += 1

    if score >= 50:
        game_is_running = False
        print("Wow you got all of the states!")

print(correct_guesses)
print(f"Your final score is {score}")
missed_states = []

for state in data.state:
    if state not in correct_guesses:
        location = data[data.state == state]
        missed_states.append(state)
        write_state(name_state=state, x=int(location.x), y=int(location.y))

missed_states_data = pandas.DataFrame(missed_states)
missed_states_data.to_csv("states_to_learn.csv")

screen.exitonclick()

