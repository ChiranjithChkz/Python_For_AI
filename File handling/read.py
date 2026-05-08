# file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()


file.read(10)       # Read first 10 characters
file.readline()     # Read one line
file.readlines()    # Read all lines into a list