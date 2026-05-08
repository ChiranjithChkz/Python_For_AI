# 🔹 When to use class methods

# You need to modify class-level variables
# You want to create factory methods (alternative constructors)

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population
    
p1 = Person("Alice")
p2 = Person("Hero")

print("Population number: ",Person.get_population())