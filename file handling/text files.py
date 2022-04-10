print("We are going to see how to open, read and write into .txt files here")

text_file = open("test.txt")

# The below would throw and error as we do not have the random file in the directory we are working in.
# wrong_file = open("random.txt")

# To know the encoding of the file opened.
print(text_file.encoding)

# Name of the file we are working with
print(text_file.name)

# Mode in which the file is opened
print(text_file.mode)

print(text_file.buffer)
print("\n")

# To check if the file is closed or open
print(text_file.closed)

# The level of error handling mechanism being used
print(text_file.errors)

# Check if the buffering is set at line level
print(text_file.line_buffering)

# Check for newline character being used
print(text_file.newlines)

# Return the integer “file descriptor” for the current file
print(text_file.fileno())
print("\n")

print("Reading from the file")
# Reads two bytes from the file
print(text_file.read(2))

# Reads the current line from the cursor
print(text_file.readline())

print("Going to print readlines () output")
# Reads lines from the cursor and returning them as a list
print(text_file.readlines())

print(text_file.seekable())
print(text_file.readable())
print(text_file.writable())

print("Reading from start again")
print(text_file.seek(0))
print(text_file.readlines())
print("\n")

print("Closing the file and opening in write mode. Note: This will delete the contents in the file once opened")
text_file.close()
text_file = open("test.txt", "w")
print(text_file.writable())
print(text_file.readable())
cont = []
cont.append("Line x written by Python\n")
cont.append("Line y\n")
print(cont)
text_file.writelines(cont)
text_file.close()
print("Written two lines and closed the file")

print("Opening the file and reading all the lines now")
text_file = open("test.txt")
print(text_file.readlines())
text_file.close()
print("\n")

print("Re-opened the file in append mode. We cannot read the file. write will append to the file at the end.")
text_file = open("test.txt","a")
print(text_file.readable())
print(text_file.writable())
text_file.write("Line z\n")
# Seek works only when the file is opened in read mode. In write and append mode it wouldn't work
# text_file.seek(0)
text_file.write("Line a\n")
text_file.close()
print("\n")

print("Re-opened the file in r+ mode i.e, read and write. Can read the file and append at the end")
text_file = open("test.txt", "r+")
print(text_file.readable())
print(text_file.writable())
text_file.write("Line b in r+ mode\n")
# Below will only read what is present in the file before the current edits.
print(text_file.readlines())
text_file.close()
print("\n")

print("Creating a new filw altogether. Following fails if the file already present")
file2 = open("test2.txt","x")
print(file2.writable())
file2.write("A new file created by python")
file2.close()
print("\n")

print("More on open() in : https://docs.python.org/3/library/functions.html#open")
print("More on open modes in : https://docs.python.org/3.8/library/io.html?highlight=flush#raw-file-i-o")
