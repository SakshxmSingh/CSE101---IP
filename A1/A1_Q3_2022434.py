# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques03------------------
x0 = int(input())
y0 = int(input())

dist = []
n,s,e,w = 0,0,0,0

f = True
while f:
    x = int(input())
    if x>0:
        dist.append(x)
    else:
        f = False

for i in dist:
    if i<=25:
        n+=i
    elif 26<=i<=50:
        s+=i
    elif 51<=i<=75:
        e+=i
    elif i>=76:
        w+=i

x = e - w + x0
y = n - s + y0

print("final coordinates are: ("+str(x)+","+str(y)+")")                                 #co-ordinates
print("Distance travelled: ",(n+s+e+w))                                                 #distance
print("Straight distance from start point",((x-x0)**2 + (y-y0)**2)**(1/2))              #displacement
