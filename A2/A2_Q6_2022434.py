# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------ques06------------------
wts = [(20,5),(20,5),(100,25),(30,15),(20,5),(20,5),(120,40)]
file = open('/Users/saksham/Desktop/Programming/CSE101 - IP/A2/IPmarks.txt', 'r')

d_input = {}
for i in file:
    lst = (i.split(', '))
    d_input.update({int(lst[0]):list(map(int,lst[1:]))})

d_calculated = {}
for key in d_input:
    total = 0
    for i in range(len(d_input[key])):
        total+=(d_input[key][i]/wts[i][0])*(wts[i][1])
    d_calculated.update({key:round(total)})

d_grades = {}
for key in d_calculated:
    if d_calculated[key]>80:
        d_grades.update({key:'A'})
    elif 70<d_calculated[key]<=80:
        d_grades.update({key:'A-'})
    elif 60<d_calculated[key]<=70:
        d_grades.update({key:'B'})
    elif 50<d_calculated[key]<=60:
        d_grades.update({key:'B-'})
    elif 40<d_calculated[key]<=50:
        d_grades.update({key:'C'})
    elif 35<d_calculated[key]<=40:
        d_grades.update({key:'C-'})
    elif 30<=d_calculated[key]<=35:
        d_grades.update({key:'D'})
    elif 30>d_calculated[key]:
        d_grades.update({key:'F'})

file_2 = open('/Users/saksham/Desktop/Programming/CSE101 - IP/A2/IPgrades','w')
for key in d_calculated:
    file_2.write(str(key)+', '+str(d_calculated[key])+', '+str(d_grades[key]+'\n'))
