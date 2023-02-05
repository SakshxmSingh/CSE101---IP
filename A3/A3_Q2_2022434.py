# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 03

#--------------ques02------------------
file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/sorted_data.txt")

dic1 = {}
for i in file:
    tmp = i.split(', ')
    name  = tmp[0]
    tmp2 = {'ENTRY':'','EXIT':''}