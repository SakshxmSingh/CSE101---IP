# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 03

#--------------ques05------------------
def cuttoff_decider(scale):
    diff_lust = []
    if len(scale)==1:
        cuttoff = scale[0]
    elif len(scale)==2: 
        diff_lust.append((scale[1][1],0,0))
        cuttoff = (scale[diff_lust[0][1]+1][1] + scale[diff_lust[0][2]+1][1])/2
    elif len(scale)>2:
        for i in range(2,len(scale)):
            diff = scale[i-1][1]-scale[i][1]
            diff_lust.append((diff, i-1, i))
        diff_lust.sort(key=lambda row: row[0], reverse=True)
        cuttoff = (scale[diff_lust[0][1]][1] + scale[diff_lust[0][2]][1])/2
    # elif len(scale)==1:
    #     cuttoff = scale[0]
    # elif len(scale)==2: 
    #     diff_lust.append((scale[1][1],0,0))
    #     cuttoff = (scale[diff_lust[0][1]][1] + scale[diff_lust[0][2]][1])/2
    # elif len(scale)==1:
    #     cuttoff = scale[0]
    print(cuttoff)
    return cuttoff

cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
policy = {80, 65, 50, 40}
f_input = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/marks.txt","r+")

global data, sum_data
data = []
for i in f_input: data.append(list(map(int,(i.split(", ")))))
sum_data = []
for i in data: sum_data.append((i[0],sum(i[1:])))
sum_data.sort(key=lambda row: row[1], reverse=True)

grade_data,a_scale,b_scale,c_scale,d_scale = [],[80],[65],[50],[40]
for x in sum_data:
    # if x[1]>82: grade_data.append((x[0], 'A'))
    # elif 78>x[1]>67: grade_data.append((x[0], 'B'))
    # elif 63>x[1]>52: grade_data.append((x[0], 'C'))
    # elif 48>x[1]>42: grade_data.append((x[0], 'D'))
    # elif x[1]<38: grade_data.append((x[0], 'F'))
    if 82>=x[1]>=78: a_scale.append(x)
    elif 67>=x[1]>=63: b_scale.append(x)
    elif 52>=x[1]>=48: c_scale.append(x)
    elif 42>=x[1]>=38: d_scale.append(x)

def cuttoff_decider(scale):
    diff_lust = []
    if len(scale)==1:
        cuttoff = scale[0]
    elif len(scale)==2: 
        diff_lust.append((scale[1][1],0,0))
        cuttoff = (scale[diff_lust[0][1]+1][1] + scale[diff_lust[0][2]+1][1])/2
    elif len(scale)>2:
        for i in range(2,len(scale)):
            diff = scale[i-1][1]-scale[i][1]
            diff_lust.append((diff, i-1, i))
        diff_lust.sort(key=lambda row: row[0], reverse=True)
        cuttoff = (scale[diff_lust[0][1]][1] + scale[diff_lust[0][2]][1])/2
    # elif len(scale)==1:
    #     cuttoff = scale[0]
    # elif len(scale)==2: 
    #     diff_lust.append((scale[1][1],0,0))
    #     cuttoff = (scale[diff_lust[0][1]][1] + scale[diff_lust[0][2]][1])/2
    # elif len(scale)==1:
    #     cuttoff = scale[0]
    print(cuttoff)
    return cuttoff

cuttoff_decider(d_scale)

def func_1():
    pass

def func_2():
    pass

