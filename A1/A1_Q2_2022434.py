# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques02------------------
X = []
Y = []
for x in range(50):
    for y in range(50):
        if 8*x+2*y==400 and 2*x+y==120 and x>=0 and y>=0:
            X.append(x)
            Y.append(y)

profit=0
M = int(input("Enter M: "))

if M<max(X) and M<max(Y):
    profit += 90*M+25*M
    profit += 100*(max(X)-M)+30*(max(Y)-M)
elif M<max(X) and M>=max(Y):
    profit += 90*M+25*max(Y)
    profit += 100*(max(X)-M)
if M>=max(X) and M<max(Y):
    profit += 90*max(X)+25*M
    profit += 30*(max(Y)-M)
if M>=max(X) and M>=max(Y):
    profit += 90*max(X)+25*max(Y) 

print("The max profit is",profit,"USD and it is obtained by selling",max(X), "units of tables and",max(Y),"units of chairs")
