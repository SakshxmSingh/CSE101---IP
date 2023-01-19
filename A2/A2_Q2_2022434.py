# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------ques02------------------
grades = {'A+':10,'A':10,'A-':9,'B':8,'B-':7,'C':6,'C-':5,'D':4,'F':2}
input_list= [tuple(input("Enter course, credits, and grade: \n").split())]
while input_list[-1]!=():
    if len(input_list[-1][0])==6 and (input_list[-1][0][:3].isupper() or input_list[-1][0][:4].isupper()) and (input_list[-1][0][3:6].isdigit() or input_list[-1][0][4:6].isdigit()):
        pass
    else:
        print('improper course no')
        input_list.pop()
    if int(input_list[-1][1])!=1 and int(input_list[-1][1])!=2 and int(input_list[-1][1])!=4:
        print('incorrect credit')
        input_list.pop()
    elif input_list[-1][2] not in grades:
        print('incorrect grade')
        input_list.pop()

    input_list.append(tuple(input().split()))
input_list.pop()

total_credits = 0
for i in input_list:
    total_credits += int(i[1])

sgpa = 0
for i in input_list:
    sgpa += (int(i[1])*grades[i[2]])/total_credits
    print(i[0]+": "+i[2])

print("SGPA: "+str(round(sgpa,2)))
