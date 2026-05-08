#A property lets you access a method without using parentheses, just like a variable.
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.math = math
        self.chem = chem

    @property
    def percentage(self):
        return str((self.chem + self.math + self.phy) / 3) + "%"
        
stu1 = Student(98, 99, 95)
print(stu1.percentage)


stu1.phy = 12
print(stu1.percentage)