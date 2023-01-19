# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques09-------------------
def demand(p):
    d=(2.7182)**(10 - 1.05*p)
    return d

def supply(p):
    s=(2.7182)**(1+1.06*p)
    return s

price = 1.0
while demand(price)>supply(price):
    price+=price*0.05
    if demand(price)==supply(price):
        break
if demand(price)!=supply(price):
    print("there is no soln")
    print("Nearest equilibrium for the demand and supply is between",demand(price),"and",supply(price),"and at the price of",price)
else:
    print("equilibrium for the demand and supply is at",demand(price),"and at the price of",price)
