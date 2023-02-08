# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 03

#--------------ques03------------------
import random

def F1():
    global specs, string
    lust = string.split()
    lust = [i.lower() for i in lust]
    # for i in range(len(lust)):
    #     for j in specs:
    #         if j in lust[i]:
    #             lust[i] = lust[i].strip(j)
    lust = ["".join(chr for chr in i if chr.isalnum()) for i in lust]
    lust_set = set(lust)
    return len(lust_set)/len(lust), lust_set

def F2():
    global specs, string
    lust = string.split()
    lust = [i.lower() for i in lust]
    lust = ["".join(chr for chr in i if chr.isalnum()) for i in lust]
    lust_set = set(lust)
    dic = {}
    for key in lust_set:
        value = lust.count(key)
        dic[key]=value
    dic_sort = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
    lust2 = []
    for keys in dic_sort:
        lust2.append(dic_sort[keys])
        if len(lust2)==5:
            break
    
    return sum(lust2)/len(lust) , dic_sort

def F3():
    global specs, string
    sent = string.split(".\n")
    string = ". ".join(sent)
    split_indices = [0]
    # for i in range(len(string)):
    #     if string[i] == '.':
    #         if i == len(string)-1:
    #             if string[i-1]=='.' or string[i-1]==',':
    #                 pass
    #             else:
    #                 split_indices.append(i+2)
    #         else:
    #             if string[i-1]=='.' or string[i-1]==',' or string[i+1]=='.' or string[i+1]==',':
    #                 pass
    #             else:
    #                 split_indices.append(i+2)
    # sent = [string[i:j] for i,j in zip(split_indices, split_indices[1:]+[None])]
    # sent = string.split(". ")
    sent = string.split(". ")
    sent.pop()
    # print(sent, len(sent))
    count = 0
    for i in sent:
        if len(i.split())>35 or len(i.split())<5:
            count+=1
    return count/len(sent)

def F4():
    global specs, string
    lust = string.split()
    lust = [i.lower() for i in lust]
    lust = ["".join(chr for chr in i if chr.isalnum()) for i in lust]
    count = 0
    # for i in range(len(string)):
    #     if string[i] in specs:
    #         if string[i-1] in specs or string[i+1] in specs:
    #             count+=1

    for i in string.split():
        count_temp = 0
        for j in i:
            if j in specs:
                count_temp+=1
        if count_temp>1:
            count+=1
    
    return count/len(lust)

def F5():
    global specs, string
    if len(string.split())>750:
        return 1
    else:
        return 0

specs = [',','.',':',';']
f_output = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/scores.txt","a+")

for i in range(1,5):
    f_input = open(f"/Users/saksham/Desktop/Programming/CSE101 - IP/A3/file{i}.txt","r+")
    string = f_input.read()
    
    netscore = 4 + F1()[0]*6 + F2()[0]*6 - F3() - F4() - F5()
    # f_output.write(f"file{i}\nscore: {netscore}\n")
    f_output.write(f"file{i}\nscore: {netscore}\n")
    temp = []
    for k in F2()[1]:
        temp.append(k)
        if len(temp)>=5:
            break
    f_output.write("most used words: "+str(temp)+"\nrandom words: ")
    for i in range(5):
        f_output.write(random.choice(tuple(F1()[1]))+', ')
    f_output.write("\n------------------------------\n")
