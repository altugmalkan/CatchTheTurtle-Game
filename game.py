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
leonardo.speed(3)
leonardo.turtlesize(2)

score_turtle = turtle.Turtle()
score_turtle.hideturtle()

time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.color("blue")

def getPosition(x,y):
    global score
    distance = leonardo.distance(x, y)
    if distance < 20:
        score += 1

score = 0
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
    time_turtle.clear()
    score_turtle.clear()
    leonardo.showturtle()
    leonardo.onclick(getPosition)
    i-=1
    time.sleep(0.5)

game_over_turtle = turtle.Turtle()
game_over_turtle.hideturtle()
game_over_turtle.penup()
game_over_turtle.setposition(0,0)
game_over_turtle.pendown()
game_over_turtle.write("GAME OVER !",font=("Arial",40,"bold") ,align="center")

score_turtle.penup()
score_turtle.setposition(0,-100)
score_turtle.pendown()
score_turtle.write("Your final score: " + str(score),font=("Arial",32,"bold") ,align="center")

screen.mainloop()
