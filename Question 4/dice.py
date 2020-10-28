"""
    dice.py 
    Author: Byrce Streeper
    Date: 10/27/2020

    Project: Returns an estimation for pi only using a simulation of dice rolls.
"""
Project: 
import random

#Return wheteher two cartesian points are within the unit circle
def incircle(x,y):
    return ((x**2)+(y**2))<1

#Returns a random dice roll -1 
def rollDice():
    return float(random.choice([0,1,2,3,4,5]))

#Generates a random point and returns whether a point is in a unit circle 
def getPoint():
    x, y, step = 0, 0, 1/6
    while True:
        if incircle(x,y) and incircle(x+step*6, y+step*6):
            return True
        if not incircle(x,y):
            return False
        x+=rollDice()*step
        y+=rollDice()*step
        step /= 6

#Runs Montecarlo simulation with n trials 
def sim(n):
    inside=0
    for i in range(n):
        if getPoint():
            inside+=1

    print("Inside Circle: ", inside)
    print("Total Trials: ", n)
    print("Pi Estimation: ",float(inside)*4/n)


sim(100000)