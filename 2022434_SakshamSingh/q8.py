class Student:
    def __init__(self,rollno,name):
        self.rollno = int(rollno)
        self.name = name
        self.courses = {}

    def add_course(self,key,grade):
        grade = int(grade)
        self.courses.update({key:grade})

    def avg(self):                          # to take avg of grades
        sum = 0
        for key in self.courses:
            sum+=self.courses[key]
        avg = sum/len(self.courses)
        return avg

    def printrecord(self):
        print("Name: "+self.name+"\nRollno: "+str(self.rollno)+"\nCourse record: ")
        for key in self.courses:
            print(key+"\t"+str(self.courses[key]))
        print("Average grade: "+ str(self.avg()))



s1 = Student(23001,"stu1")              # making a new student object
s1.add_course("cs101",9)                # adding courses with grade
s1.add_course("M101",8)

s1.printrecord()                        # printing the record
