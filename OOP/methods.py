#method(like function) inside class
# data(attributes)

class Student:

    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
    def welcome(self): #method
        print("Welcome student", self.name)

    def get_marks(self): #method
        return self.marks

s1 = Student("karan", 97) #object
s1.welcome()
print(s1.get_marks())