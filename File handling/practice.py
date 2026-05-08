#with open("practice.txt", "w") as f:
    # f.write("Hi everyone\n we are learning file I/O\n")
    # f.write("using Java.\n Like programming in Java.")

#replace Java-> Python

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)


with open("practice.txt","w") as f:
    f.write(new_data)
    
# import os

# os.replace()