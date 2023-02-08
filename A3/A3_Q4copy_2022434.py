# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 03

#--------------ques04 copy for q6------------------
import time

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

def func_1(cname,credits,assessments,data):
    print("Course name: "+cname+"\t\t"+"Credits: "+str(credits)+"\nAssessments:")
    for i in assessments:
        print(i[0],end='\t')
    print()
    for i in assessments:
        print(i[1],end="\t")
    print()
    print("Cutoffs:\nA:",cuttoff_decider(a_scale),"\tB:",cuttoff_decider(b_scale),"\tC:",cuttoff_decider(c_scale),"\tD:",cuttoff_decider(d_scale))
    a,b,c,d,f=0,0,0,0,0
    for i in data:
        if i.grade=='A': a+=1
        elif i.grade=='B': b+=1
        elif i.grade=='C': c+=1
        elif i.grade=='D': d+=1
        elif i.grade=='F': f+=1
    print("Grades summary: \nA:",a,"\tB:",b,"\tC:",c,"\tD:",d,"\tF:",f)

def func_2(data):
    f_output = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/grades.txt","w+")
    f_output.write("RollNo.\t\tTotal\tGrade\n")
    for i in data:
        f_output.write(str(i.rno)+"\t\t"+str(i.total)+"\t\t"+str(i.grade)+"\n")

def func_3(rno_input,data):
    for i in data:
        if rno_input not in [j.rno for j in data]:
            break
        elif rno_input==i.rno:
            print("Roll No.: ",rno_input)
            print("Assesment marks: ",i.marks)
    for i in data:
        if rno_input not in [j.rno for j in data]: 
            print("Rollno doesn't exist") 
            break
        elif rno_input==i.rno:
            print("Total marks: ",i.total,"\nFinal Grade: ",i.grade)

class Courses:
    def __init__(self, coursename, credits, assessments):
        self.coursename = coursename
        self.credits = credits
        self.assessments = assessments
        self.rawdata = []
        self.data = []
        
    def create_assesment(self, file):
        for i in file: self.rawdata.append(list(map(int,(i.split(", ")))))
        for i in self.rawdata: 
            x = Student(i[0],i[1:])
            self.data.append(x)
        self.data.sort(key=lambda x : x.total, reverse=True)
        
        for i in self.data: 
            if 82>=i.total>=78: a_scale.append((i.rno, i.total))
            elif 67>=i.total>=63: b_scale.append((i.rno, i.total))
            elif 52>=i.total>=48: c_scale.append((i.rno, i.total))
            elif 42>=i.total>=38: d_scale.append((i.rno, i.total))
            
        start=time.time()
        for j in range(1000):
            for i in self.data:
                if i.total>=cuttoff_decider(a_scale): i.assign_grades('A')
                elif cuttoff_decider(a_scale)>i.total>=cuttoff_decider(b_scale): i.assign_grades('B')
                elif cuttoff_decider(b_scale)>i.total>=cuttoff_decider(c_scale): i.assign_grades('C')
                elif cuttoff_decider(c_scale)>i.total>=cuttoff_decider(d_scale): i.assign_grades('D')
                elif cuttoff_decider(d_scale)>i.total: i.assign_grades('F')
        end=time.time()
        print(end-start)

class Student:
    def __init__(self, rno, marks):
        self.rno = rno
        self.marks = list(marks)
        self.total = sum(self.marks)
        self.grade = ''

    def __str__(self) -> str:
        return str(self.rno)+'\t'+str(self.marks)+'\t'+str(self.total)+'\t'+str(self.grade)

    def assign_grades(self, parm):
        self.grade = parm

global a_scale,b_scale,c_scale,d_scale
a_scale,b_scale,c_scale,d_scale = [80],[65],[50],[40]
cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assign.", 30), ("endsem", 25)] 
f_input = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/marks.txt","r+")

IP = Courses(cname,credits,assessments)
IP.create_assesment(f_input)

if __name__ == "__main__":
    while True:
        x = (input("Enter function:\n1. Course summary\n2. Student Grades\n3. Search Student\n"))
        try:
            if int(x)==1:
                func_1(cname,credits,assessments,IP.data)
            elif int(x)==2:
                func_2(IP.data)
            elif int(x)==3:
                roll=int(input("Enter rno: "))
                start=time.time()
                func_3(roll,IP.data)
                end=time.time()
                print(end-start)
            else:
                break
        except ValueError:
            break