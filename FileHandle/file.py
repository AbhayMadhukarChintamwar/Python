
# This is for reading a file using the with statement, which ensures that the file is properly closed after its suite finishes, even if an exception is raised. The code reads each line from "file.txt" and prints it to the console.
with  open("file.txt","r") as f:
    for line in f:
        print(line)

# This is for writing to a file using the with statement. It opens "file.txt" in write mode ("w"), which will create the file if it doesn't exist or overwrite it if it does. The code writes the string "Hello, World!" to the file.
with open("file.txt","w") as f:
    f.write("Hello, World!")
    f.writelines(["\nThis is a new line.", "\nThis is another line."])
