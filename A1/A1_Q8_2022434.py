# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques08-------------------
def sum(list):
    y = 0
    for i in list:
            y+=i
    return y 

pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
growth_rate =[]
for i in range(0,len(pop)):
    growth_rate.append((2.5 - 0.4*i)/100)                   # making the grwoth rate list

years = 0

while sum(growth_rate)>0:
    for i in range(len(pop)):                               # applying the growthrate on every element of pop list
        pop[i]+=pop[i]*growth_rate[i]
    for j in range(len(growth_rate)):
        growth_rate[j]=growth_rate[j]-0.001                 # decreasing every element of growth rate
    years+=1                                                # increasing the years

print("max population is",round(sum(pop)/1000, 4),"billions and it is reached in",years,"years")


