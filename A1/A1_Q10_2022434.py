# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques10-------------------
def f(x):
    y = x**3 - 10.5*x**2 + 34.5*x - 35
    return y

def g(x):
    y = 3*x**2 - 21*x + 34.5
    return y

def root_finder(f,g,x):
    roots = []
    if round(f(x),3)==0:
        roots.append(round(x,2))
        for i in range(100):
            y = x+i
            z = x-i
            while round(f(y),3)!=0:
                y = y - f(y)/g(y)
            if round(f(y),3)==0:
                roots.append(round(y,2))
            while round(f(z),3)!=0:
                z = z - f(z)/g(z)
            if round(f(z),3)==0:
                roots.append(round(z,2))
    else:
        while round(f(x),3)!=0:
            x = x - f(x)/g(x)
        if round(f(x),3)==0:
            roots.append(round(x,2))
            for i in range(100):
                y = x+i
                z = x-i
                while round(f(y),3)!=0:
                    y = y - f(y)/g(y)
                if round(f(y),3)==0:
                    roots.append(round(y,2))
                while round(f(z),3)!=0:
                    z = z - f(z)/g(z)
                if round(f(z),3)==0:
                    roots.append(round(z,2))       
    roots_2=[]
    for i in roots:
        if i not in roots_2:
            roots_2.append(i)
    print("the three roots are: ",roots_2)

root_finder(f,g,float(input("Enter x0: ")))
