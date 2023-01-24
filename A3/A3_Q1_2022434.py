# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 03

#--------------ques01------------------
def mountain(n,g=0):
    i = n
    if i==0:
        pass
    else:
        print("* "*i+"  "*(2*g)+"* "*i)
        i-=1
        g+=1
        mountain(i,g)

def valley(i=2):
    global n
    if i==n+1:
        pass
    else:
        print("* "*(i)+"  "*(2*n-2*i)+"* "*(i))
        i+=1
        valley(i)

n = int(input("Enter n: "))

mountain(n)
valley()
