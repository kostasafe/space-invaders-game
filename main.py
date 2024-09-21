import turtle
import os
import math
import random

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

#Score 
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 275)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

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
        x = +280
    player.setx(x)

def fire_gun():
    #declare gunstate as a global
    global gunstate
    if gunstate == "ready":
        gunstate = "fire"
        #gun position just above player
        x = player.xcor()
        y = player.ycor() + 10
        gun.setposition(x,y)
        gun.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False
     
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



#Number of enemies
number_of_enemies = 5
#List
enemies = []

#Add enemies in list
for i in range(number_of_enemies):
     #enemy creation
     enemies.append(turtle.Turtle())

#Enemies
for enemy in enemies:
        #enemy = turtle.Turtle()
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

enemyspeed = 2

#Game loop
while True:

    for enemy in enemies:
        #enemy movement
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        if enemy.xcor() > +280:
            for e in enemies: #to move all enemies down if one touches the side
                y = e.ycor()
                y -=  40
                e.sety(y)
            enemyspeed *= -1
        
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -=  40
                e.sety(y)
            enemyspeed *= -1


        #collision check between enemy and shot
        if isCollision(gun, enemy):
            #reset shot
            gun.hideturtle()
            gunstate = "ready"
            gun.setposition(0, -400)
            #Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #score count
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))



        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break

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