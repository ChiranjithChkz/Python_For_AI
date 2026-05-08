class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi ", self.name , "Your avg marks is ", sum/3)
      
s1 = Student("Hero honda", [97, 98, 97])
s1.get_avg()

s1.name = "Captain America"