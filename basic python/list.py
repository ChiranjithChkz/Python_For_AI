fruits= ["apple", "orange", "coconut","pepaya","lemon", "watermelon"] 
# this is a list 
# we can excess it buy using index number
print(fruits)
print(fruits[0:2])
# range
print(fruits[::-1]) 
# reverse

# for fruit in fruits:
    # print(fruit)
# iteration


# print(dir(fruits))
# print(help(fruits))
# len
print(len(fruits))
# boolean
print("apple" in fruits)

fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)



# fruits.append("pineapple")
#fruits.remove("pineapple")
#fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()

# print(fruits.index("orange"))
print(fruits.count("banana"))

print(fruits)