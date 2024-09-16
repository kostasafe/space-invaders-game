import turtle
import os

#seting up screen
myscreen = turtle.Screen()
myscreen.bgcolor("black")
myscreen.title("Space Invaders")

#Border drawing
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Player Turtle
player = turtle.Turtle()
player.color("yellow")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#Player Movement Left-Right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x <-280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > +280:
        x= +280
    player.setx(x)

def fire_gun():
    #declare gunstate as a global
    global gunstate
    if gunstate == "ready":
        gunstate = "fire"
        #gun position just above player
        x = player.xcor()
        y = player.ycor() +10
        gun.setposition(x,y)
        gun.showturtle()

#Keyboard Bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_gun, "space")

#Player's Gun
gun = turtle.Turtle()
gun.color("blue")
gun.shape("triangle")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(0.5, 0.5)
gun.hideturtle()

gunspeed = 20

#Define gun state
#ready - ready to fire
#fire - gun is firing
gunstate = "ready"


#Enemies
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2

#Game loop
while True:

    #enemy movement
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    
    if enemy.xcor() > +280:
        y = enemy.ycor()
        y -=  40
        enemyspeed *= -1
        enemy.sety(y)
    
    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -=  40
        enemyspeed *=-1
        enemy.sety(y)

    #bullet movement
    if gunstate == "fire":
        y = gun.ycor()
        y += gunspeed
        gun.sety(y)

    #check if bullet reached top border
    if gun.ycor() > 275:
        gun.hideturtle()
        gunstate = "ready"

delay =  input("Press enter to finish.")