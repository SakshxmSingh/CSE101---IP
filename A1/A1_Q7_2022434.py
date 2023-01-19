# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques07-------------------

cost = int(input("Enter cost of laptop:  "))
allowance = 20000
sf = 0.1
rate = 0.005

savings = allowance*sf
account = 0
months = 1
account+=savings
while account <= cost:
    account+=account*rate
    account+=savings
    # print(account)
    months+=1

print("No of months it took:", months)
print("Money left in account:",account-cost) 