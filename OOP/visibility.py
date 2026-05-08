#private
#how to access private
class Person:
    __name = "anonymous"

    def __hello(self): #private method
        print("Hello Person")

    def welcome(self):
        self.__hello()

s1 = Person()
print(s1.welcome())