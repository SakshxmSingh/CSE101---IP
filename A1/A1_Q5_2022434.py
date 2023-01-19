# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques05-------------------
def fact(x):
    y = 1
    for i in range(1,x+1):
        y = y*i
    return y

def cos(x):
    y=0
    for i in range(0,69):
        y = y + ((-1)**i)*(x**(2*i))/(fact(2*i))
    return y

def sin(x):
    y=0
    for i in range(0,69):
        y = y + ((-1)**i)*(x**(2*i+1))/(fact(2*i+1))
    return y

def tan(x):
    y = sin(x)/cos(x)
    return y


angle = int(input("Enter angle: "))
angle_rads = (angle/180)*3.14159
dist = int(input("Enter distance: "))

print("height of pole:",round(tan(angle_rads)*dist,3))
print("length of person from the top of the pole:",round(dist/cos(angle_rads),3))
