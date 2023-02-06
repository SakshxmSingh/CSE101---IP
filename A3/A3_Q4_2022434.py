# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 03

#--------------ques04------------------
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
        # for i in self.data: print(i)


class Student:
    def __init__(self, rno, marks):
        self.rno = rno
        self.marks = list(marks)
        self.total = sum(self.marks)
        self.grade = ''

    def __str__(self) -> str:
        return str(self.rno)+'\t'+str(self.marks)+'\t'+str(self.total)

    def assign_grades(self, cutoffs):
        pass

    

cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assign.", 30), ("endsem", 25)] 
f_input = open("/Users/saksham/Desktop/Programming/CSE101 - IP/A3/marks.txt","r+")

IP = Courses(cname,credits,assessments)
IP.create_assesment(f_input)

