with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

    #don't need to close


with open("demo.txt", "w") as f:
    f.write("new data")
    