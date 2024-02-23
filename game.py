import random
import turtle
import time 


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
screen.screensize(1800,900)

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("blue")


score_turtle = turtle.Turtle()
score_turtle.hideturtle()

time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.color("blue")

score = 0

def getPosition(x,y):
    global score
    distance = leonardo.distance(x, y)
    if difficulty == "easy":    
        if distance < 50:
            score += 1
    elif difficulty == "medium":
        if distance < 35:
            score += 1
    elif difficulty == "hard":
        if distance < 20:
            score += 1

def game(diff):
    if diff == "easy":
        leonardo.speed(10)
        leonardo.turtlesize(4)
        sec = 0.5
    elif diff == "medium":
        leonardo.speed(3)
        leonardo.turtlesize(3)
        sec = 0.35
    elif diff == "hard":
        leonardo.speed(0)
        leonardo.turtlesize(2)
        sec = 0.2
    i=20
    while i>0:
        time_turtle.penup()
        time_turtle.setposition(0,300)
        time_turtle.pendown()
        time_turtle.write("Time: " + str(i), align= "center" , font=("Arial", 24, "bold"))
        score_turtle.penup()
        score_turtle.setposition(0,250)
        score_turtle.pendown()
        score_turtle.write("Score: " + str(score), align= "center" , font=("Arial", 24, "bold"))

        randPositionX = random.randint(0,500) - 250
        randPositionY = random.randint(0,500) - 250
        leonardo.penup()
        leonardo.hideturtle()
        leonardo.goto(x=randPositionX,y=randPositionY)
        leonardo.showturtle()
        leonardo.onclick(getPosition)
        time_turtle.clear()
        score_turtle.clear()
        i-=1
        time.sleep(sec)
    screen.clear()
    screen.bgcolor("light blue")
    game_over_turtle = turtle.Turtle()
    game_over_turtle.hideturtle()
    game_over_turtle.penup()
    game_over_turtle.color("red")
    game_over_turtle.setposition(0,0)
    game_over_turtle.pendown()
    game_over_turtle.write("GAME OVER !",font=("Arial",40,"bold") ,align="center")

    score_turtle.penup()
    score_turtle.setposition(0,-100)
    score_turtle.color("red")
    score_turtle.pendown()
    score_turtle.write("Your final score: " + str(score),font=("Arial",32,"bold") ,align="center")

difficulty_turtle=turtle.Turtle()
difficulty_turtle.hideturtle()
difficulty_turtle.penup()
difficulty_turtle.setposition(0,100)
difficulty_turtle.pendown()
difficulty_turtle.write("Welcome to Catch the Turtle!", align="center", font=("Arial", 24, "bold"))

difficulty = screen.textinput("Game Difficulty", "Please select the game difficulty (easy/medium/hard): ").lower()

while difficulty not in ["easy", "medium", "hard"]:
    difficulty = screen.textinput("Invalid Input", "Invalid difficulty! Please select again:(easy,medium or hard) ").lower()

difficulty_turtle.write(f"You've selected {difficulty} difficulty. Let's start the game!", align="center", font=("Arial", 24, "bold"))
difficulty_turtle.clear()
game(difficulty)

screen.mainloop()
