from random import uniform
from math import sqrt
from time import time


#Ask the user for the number of darts they would like to 
darts=int(input("How many darts do you want to throw? "))
print("")


#starts the computation time
start_time=time()


#sets the initial number of darts inside the circle as zero
darts_inside=0



#draws the number of darts that the user asked for 
for dart in range(darts):
    

    #sets the darts to be random floats between the coordinates of the square
    x=uniform(-200,200)
    y=uniform(0,400)


    #Adds 1 to the total number of darts is the dart in thrown inside the circle
    if sqrt((x-0)**2+(y-200)**2)<=200:
        darts_inside=1+darts_inside


#calculate the approximation of pi using the number of darts inside divided by the total number of darts
pi=4*darts_inside/darts

#calculates the total time it took for the program to run
end_time=time()
comp_time=end_time-start_time

#prints number of darts thrown, the darts inside the circle, and the approximation of pi
print("darts thrown",format(darts,".0e"))
print("approximation of pi:",format(pi,".7f"))
print("computation time:",format(comp_time,".0e"),"seconds")
