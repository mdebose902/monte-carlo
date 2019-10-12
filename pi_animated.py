#imports turtle, the uniform function and the square root function
from random import uniform
from turtle import *
from math import sqrt


#sets the turtle speed to 0 and draw a circle with radius 200
speed(0)
screensize(1000,1000)
circle (200)

# move the turtle outside the circle and starts drawing the square 
penup()
goto(200,0)
pendown()
setheading(90)


#Draws a square that is 400x400 pixels 
for side in range(4):
    forward(400)
    left(90)


#Ask the user for the number of darts they would like to 
darts=int(input("How many darts do you want to throw? "))


#sets the initial number of darts inside the circle as zero
darts_inside=0



#draws the number of darts that the user asked for 
for dart in range(1,darts):

    #sets the darts to be random floats between the coordinates of the square
    x=uniform(-200,200)
    y=uniform(0,400)
    penup()
    goto(x,y)
    


    #check to see if the darts are inside the circle using the distance formula 
    if sqrt((x-0)**2+(y-200)**2)<=200:
        
        
    #makes the darts red in they land inside the circle 
        pencolor("red")

        
    #makes the starts blue if they land outside of the circle
    else:
        pencolor("blue")


    #Adds 1 to the total number of darts is the dart in thrown inside the circle
    if sqrt((x-0)**2+(y-200)**2)<=200:
        darts_inside=1+darts_inside


    #draws one dart
    pendown()
    forward(1)



# calculate the approximation of pi using the number of darts inside divided by the total number of darts
    pi=4*darts_inside/dart

    if dart %100== 0:
        print("darts thrown",format(dart,".0e"))
        print("darts inside:",darts_inside)
        print("approximation of pi:",format(pi,".7f"))
        print("")




#prints number of darts thrown, the darts inside the circle, and the approximation of pi
print("darts thrown",format(darts,".0e"))
print("darts inside:",darts_inside)
print("approximation of pi:",format(pi,".7f"))





