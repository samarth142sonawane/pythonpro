class Students:
    def getdata(self):
        self.name = input("Enter your name :")
        self.roll = int(input("Enter your Roll No. :"))
        self.java = int(input("Enter Marks of Java :"))
        self.python = int(input("Enter Marks of python :"))
    def calculate(self):
        self.total_marks = self.java + self.python 
        self.per = self.total_marks / 2
    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll}")
        print(f"Java Marks : {self.java}")
        print(f"Python Marks : {self.python}")
        print(f"Total marks : {self.total_marks}")
        print(f"You are getting : {self.per}")
s = Students()
s.getdata()
s.calculate()
s.show()







