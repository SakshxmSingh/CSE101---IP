# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 03

#--------------ques02------------------
file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/sorted_data.txt")

dic = {}
raw_data = []
for i in file:
    tmp = i.split(', ')
    key = tmp[0]
    tmp[3] = int("".join(tmp[3][:2]+tmp[3][3:5]+tmp[3][6:]))
    raw_data.append(tmp)
    if key not in dic:
        lst = [{'crossing':tmp[1],'gateno':int(tmp[2]),'time':tmp[3]}]
        dic.update({key:lst})
    else:
        dic[key].append({'crossing':tmp[1],'gateno':int(tmp[2]),'time':tmp})

# print(dic)

def F1(dic):
    name = input("Enter name: ")
    f_output = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/TA_data.txt","w+")
    lst = []
    if name in dic:
        f_output.write(name+"\n")
        for i in dic[name]:
            tup = (i['crossing'], i['gateno'], i['time'])
            lst.append(tup)
        f_output.write(str(lst))
        print("Data printed")
    else:
        print("Name doesn't exist in data")

    time_input = int(input("Enter time in 24hr time"))
    times = [i[2] for i in lst]
    # print(times)
    if time_input in times:
        if lst[times.index(time_input)][0] == "EXIT":
            print(f"{name} is exiting")
        elif lst[times.index(time_input)][0] == "ENTER":
            print(f"{name} is entering")
    else:
        for i in range(len(times)):
            if times[i] > time_input:
                if lst[i-1][0] == "EXIT":
                    print(f"{name} is not in campus")
                elif lst[i-1][0] == "ENTER":
                    print(f"{name} is in campus")
                break
    
def F2(list):
    t1 = int(input("Enter starting time: "))
    t2 = int(input("Enter ending time: "))
    enter_list = []
    exit_list = []
    for i in list:
        if t1<=int(i[3])<=t2:
            if i[1] == "ENTER":
                enter_list.append(i)
            elif i[1] == "EXIT":
                exit_list.append(i)
    f_output = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/entry-exit.txt","w+")
    f_output.write("--------------------------------\nENTRY LIST:\n--------------------------------\n")
    for i in enter_list:
        f_output.write(f"{i[0]},  {i[2]},  {str(i[3])}\n")
    f_output.write("\n--------------------------------\n")
    f_output.write("--------------------------------\nEXIT LIST:\n--------------------------------\n")
    for i in exit_list:
        f_output.write(f"{i[0]},  {i[2]},  {str(i[3])}\n")
    f_output.write("\n--------------------------------\n")

def F3():
    pass

# F2(raw_data)
print(raw_data)