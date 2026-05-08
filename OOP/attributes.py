#class and instance Attributes
class Student:
    college_name = "CUET"
    name = "anonymous" #class attribute
    #parameterized constructor
    def __init__(self, name, marks): 
        self.name = name  #obj attribute > class attribute
        self.marks = marks
        print("Adding new student in database: ")

s1 = Student("karan", 97)
print(s1.name, s1.marks)  #karan


print(Student.college_name)