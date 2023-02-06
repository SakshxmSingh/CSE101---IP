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
    return cuttoff

def func_1(cname,credits,assessments,grades):
    print("Course name: "+cname+"\t\t"+"Credits: "+str(credits)+"\nAssessments:")
    for i in assessments:
        print(i[0],end='\t')
    print()
    for i in assessments:
        print(i[1],end="\t")
    print()
    print("Cutoffs:\nA:",cuttoff_decider(a_scale),"\tB:",cuttoff_decider(b_scale),"\tC:",cuttoff_decider(c_scale),"\tD:",cuttoff_decider(d_scale))
    a,b,c,d,f=0,0,0,0,0
    for i in grades:
        if i[2]=='A': a+=1
        elif i[2]=='B': b+=1
        elif i[2]=='C': c+=1
        elif i[2]=='D': d+=1
        elif i[2]=='F': f+=1
    print("Grades summary: \nA:",a,"\tB:",b,"\tC:",c,"\tD:",d,"\tF:",f)

def func_2(grades):
    f_output = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/grades.txt","w+")
    f_output.write("RollNo.\t\tTotal\tGrade\n")
    for i in grades:
        f_output.write(str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2])+"\n")

def func_3(rno,data,grades):
    for i in data:
        if rno not in [j[0] for j in data]:
            break
        elif rno==i[0]:
            print("Roll No.: ",rno)
            print("Assesment marks: ",i[1:])
    for i in grades:
        if rno not in [j[0] for j in data]: 
            print("Rollno doesn't exist") 
            break
        elif rno==i[0]:
            print("Total marks: ",i[1],"\nFinal Grade: ",i[2])
            
cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assign.", 30), ("endsem", 25)] 
policy = [80, 65, 50, 40]
f_input = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/marks.txt","r+")

global data, sum_data
data = []
for i in f_input: data.append(list(map(int,(i.split(", ")))))
sum_data = []
for i in data: sum_data.append((i[0],sum(i[1:])))
sum_data.sort(key=lambda row: row[1], reverse=True)

grade_data,a_scale,b_scale,c_scale,d_scale = [],[80],[65],[50],[40]
for x in sum_data:
    if 82>=x[1]>=78: a_scale.append(x)
    elif 67>=x[1]>=63: b_scale.append(x)
    elif 52>=x[1]>=48: c_scale.append(x)
    elif 42>=x[1]>=38: d_scale.append(x)

for x in sum_data:
    if x[1]>=cuttoff_decider(a_scale): grade_data.append((x[0],x[1], 'A'))
    elif cuttoff_decider(a_scale)>x[1]>=cuttoff_decider(b_scale): grade_data.append((x[0],x[1], 'B'))
    elif cuttoff_decider(b_scale)>x[1]>=cuttoff_decider(c_scale): grade_data.append((x[0],x[1], 'C'))
    elif cuttoff_decider(c_scale)>x[1]>=cuttoff_decider(d_scale): grade_data.append((x[0],x[1], 'D'))
    elif cuttoff_decider(d_scale)>x[1]: grade_data.append((x[0],x[1], 'F'))


while True:
    x = (input("Enter function:\n1. Course summary\n2. Student Grades\n3. Search Student\n"))
    try:
        if int(x)==1:
            func_1(cname,credits,assessments, grade_data)
        elif int(x)==2:
            func_2(grade_data)
        elif int(x)==3:
            func_3(int(input("Enter rno: ")),data,grade_data)
        else:
            break
    except ValueError:
        break
