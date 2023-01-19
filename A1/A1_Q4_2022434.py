# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques04-------------------
import math
def integration(f,l,u,dx):
    area = 0
    x = l
    while x<=u:
        area = area + (1/2)*(f(x)+f(x+dx))*dx
        x+=dx
    print("Distance covered is",area)

def func(x):
    y = 2000*math.log(140000/(140000-2100*x))-9.8*x
    return y

lower = int(input("Enter starting time: "))
upper = int(input("Enter ending time: "))

integration(func,lower,upper,dx=0.00001)