#text files: .txt, .docx, .log
#binary files: .mp4, .mov, .png, .jpeg

#open , read and close file
# f= open("file_name/ file path", "mode")

# "r" → Read (default)
# "w" → Write (creates new or overwrites)
# "a" → Append (adds data)
# "x" → Create (fails if file exists)
# "b" → Binary mode (e.g., "rb")
# "t" → Text mode (default)


#=====I/O=============
#f= open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()