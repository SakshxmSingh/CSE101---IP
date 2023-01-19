# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------ques01------------------
menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

print("------------MENU------------\nITEMS------------------PRICE")
for i in menu:
    print(str(menu.index(i)+1),i[0]+"-"*(20-len(i[0]))+"Rs. "+str(i[1]))
print("----------------------------")

input_list= [tuple(map(int,input("Enter item number and quantity: \n").split()))]
while input_list[-1]!=():
    if input_list[-1][0] > len(menu):
        print("!!!enter valid item number!!!")
        input_list.pop()
    input_list.append(tuple(map(int,input().split())))
input_list.pop()

total_items = 0
total_cost = 0
print("-----------ORDER------------")
for i in input_list:
    print(menu[i[0]-1][0]+", "+str(i[1])+", Rs"+str(menu[i[0]-1][1]*i[1]))
    total_items += i[1]
    total_cost += menu[i[0]-1][1]*i[1]

print("TOTAL:",total_items, "items, Rs", total_cost)

