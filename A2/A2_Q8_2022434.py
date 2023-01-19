# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------ques08------------------
file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A2/URLs.txt","r")

basic_dict = {}
lstlst = []
for i in file:
    lst = [j for j in i.split(" ")]
    lst[0] = lst[0][:5]
    lst[1] = lst[1][:len(lst[1])-1]
    lst[-1] = lst[-1][:5]
    lst.pop()
    set1 = set(lst[2:])
    lst2 = [lst[0],float(lst[1]),set1]
    # basic_dict.update({lst[0]:(float(lst[1]),set1)})
    lstlst.append(lst2)

# print(lstlst)

for i in range(len(lstlst)):
    sum = lstlst[i][1]
    for j in range(len(lstlst)):
        if lstlst[i][0] in lstlst[j][2]:
            sum+=lstlst[j][1]/len(lstlst[j][2])
    basic_dict.update({lstlst[i][0]:sum})

# print(basic_dict)

sort_values = [basic_dict[key] for key in basic_dict]
# print(sort_values)
sort_values.sort(reverse=True)

n = int(input("Enter how many URLs to display: "))
if n<=len(sort_values): 
    for i in range(0,n):
        for key in basic_dict:
            if basic_dict[key]==sort_values[i]:
                print(key, sort_values[i])
elif n>len(sort_values):
    for i in range(0,len(sort_values)):
        for key in basic_dict:
            if basic_dict[key]==sort_values[i]:
                print(key, sort_values[i])
