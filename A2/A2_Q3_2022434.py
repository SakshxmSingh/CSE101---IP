# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------ques03------------------
file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A2/signatures.txt", "r")
sign_dict = {}
file_list = []
for i in file:
    file_list.append(i)
for i in range(len(file_list)):
    if file_list[i][len(file_list[i])-2]==':':
        lst = []
        j=i
        while file_list[j] != '\n':
            if j == len(file_list)-1:
                break
            else:
                j+=1
                lst.append(tuple(file_list[j].split(', ')))
        lst.pop()
        sign_dict.update({file_list[i][:len(file_list[i])-2]:lst})

numb_dict = {}
for key in sign_dict:
    n = 0
    for i in sign_dict[key]:
        n += int(i[1])
    numb_dict.update({key:n})

keymax = max(zip(numb_dict.values(), numb_dict.keys()))[1]
print("Max signatures are with "+keymax+" with",numb_dict[keymax],"signs")

keymin = min(zip(numb_dict.values(), numb_dict.keys()))[1]
print("Min signatures are with "+keymin+" with",numb_dict[keymin],"signs")
