class Complex:
    def __init__(self,r,i) -> None:
        self.real=r
        self.imaginary=i

    def __str__(self) -> str:
        return str(self.real)+" i"+str(self.imaginary)
    
    def getreal(self):
        return self.real
    def getimaginary(self):
        return self.imaginary
    def add(self,c):
        self.real+=c.getreal()
        self.imaginary+=c.getimaginary()
    def equal(self,c):
        return self.real==c.getreal()

c1 = Complex(4,5)

print(str(c1))
print(isinstance(c1,Complex))

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.gradyr = None
    def setgradyr(self, yr):
        self.gradyr = yr
    def __str__(self):
        return f'{self.name}, {self.rollno}, {self.gradyr}'


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return str([str(i) for i in self.queue])

    def add(self, person):
        self.queue.append(person)
    
    def remove(self):
        if len(self.queue)<1:
            print("Error-Empty queue")
        else:
            self.top = self.queue.pop(0)
            return self.top
    
    def isempty(self):
        if len(self.queue)<1:
            return True
        else:
            return False
    
    def length(self):
        return len(self.queue)
    
    def waiting_list(self):
        return self.queue


def studentq():
    qs = Queue()
    s1 = Student("one", 11)
    qs.add(s1)
    s2 = Student("two", 22)
    qs.add(s2)
    s3 = Student("three", 33)
    s3.setgradyr(2022)
    qs.add(s3)
    print("Student queue:", qs.length())
    print("Students:", qs)


studentq()

# q1 = Queue()
# q1.add("Saksham")
# q1.add("Swarnima")
# print(q1.remove())
# print(q1.waiting_list())
