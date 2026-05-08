#parants -> child -> grandchild
# types of inheritance
# 1. single inheritance
# 2. multi-level inheritance
# 3. multiple inheritance


#-----single inheritance--------------->
# class Car:
#     @staticmethod #common for every object in the class
#     def start():
#         print("Car started...")
    
#     @staticmethod
#     def stop():
#         print("Car stop...")


# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.name = brand

# car1 = ToyotaCar("fotuner")
# print(car1.start())


#multilevel inheritahce-------------->
# class Car:
#     @staticmethod
#     def star():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car stop...")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortune(Car):
#     def __init__(self, type):
#         self.type = type

# car1 = ToyotaCar("Disel")
# car1.star()
# car2 = Fortune("Mono")
# car2.star()
        

#====multiple inheritance========>
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

