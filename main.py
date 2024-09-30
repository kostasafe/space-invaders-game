import turtle
import os
import math
import random
from playsound import playsound
from threading import Thread

#seting up screen
myscreen = turtle.Screen()
myscreen.bgcolor("black")
myscreen.title("Space Invaders")
myscreen.bgpic("space_invaders_background.gif")
myscreen.tracer(0)

#Register the shapes
myscreen.register_shape("invader.gif")
myscreen.register_shape("player.gif")

def play_sound_async(sound_file):
    Thread(target=playsound, args=(sound_file,), daemon=True).start()

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
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Player Turtle
player = turtle.Turtle()
player.color("yellow")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0

#Player Movement Left-Right
def move_left():
    player.speed = -2

def move_right():
    player.speed = 2

def move_player() :
    x = player.xcor()
    x += player.speed
    if x > +280:
        x = +280
    if x < -280:
        x = -280
    player.setx(x)

def fire_gun():
    #declare gunstate as a global
    global gunstate
    if gunstate == "ready":
        play_sound_async('laser.wav')
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
myscreen.listen()
myscreen.onkeypress(move_left,"Left")
myscreen.onkeypress(move_right, "Right")
myscreen.onkeypress(fire_gun, "space")

#Player's Gun
gun = turtle.Turtle()
gun.color("yellow")
gun.shape("triangle")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(0.5, 0.5)
gun.hideturtle()

gunspeed = 5

#Define gun state
#ready - ready to fire
#fire - gun is firing
gunstate = "ready"



#Number of enemies
number_of_enemies = 20
#List
enemies = []

#Add enemies in list
for i in range(number_of_enemies):
     #enemy creation
     enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

#Enemies
for enemy in enemies:
        #enemy = turtle.Turtle()
        enemy.color("red")
        enemy.shape("invader.gif")
        enemy.penup()
        enemy.speed(0)
        x = enemy_start_x + (50 * enemy_number)
        y = enemy_start_y 
        enemy.setposition(x, y)
        enemy_number += 1
        if enemy_number == 10:
             enemy_start_y -= 50
             enemy_number = 0

enemyspeed = 0.2

#Game loop
while True:
    myscreen.update()
    move_player()

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
            play_sound_async('explosion.wav')
            #reset shot
            gun.hideturtle()
            gunstate = "ready"
            gun.setposition(0, -400)
            #Reset enemy
            enemy.setposition(0, 10000)
            #score count
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))



        if isCollision(player, enemy):
            play_sound_async('explosion.wav')
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
    