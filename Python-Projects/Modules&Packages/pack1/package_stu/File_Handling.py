

#File Handling /Working with the text:
## Example1: Writing data in to the text file

file = open("D:\PYTHON-PROJECTS\demofile\demo.txt", 'w')  #this is use to open the file
file.write("This is my first statemtent....\n")   # it is use to write statment in the txt file.
file.write("This is my second statemtent....\n")
file.write("This is my Third statemtent....\n")
file.write("This is my Fourth statemtent....\n")
file.write("This is my Fifth statemtent....\n")
file.write("This is my sixth statemtent....\n")
file.close()   #when ever we opne the file we need to close it.
print("program completed")

## Reading data from the text file

file = open("D:\PYTHON-PROJECTS\demofile\demo.txt", 'r')   # Here firt we are opening the file in read mode by 'r'
#print(file.read())             # this will read the existing data from the file to the IDE output
print("Using readline method")
#print(file.readline())     #this will print only the first line from the file.
print(file.readlines())   #This will print the output of the file in real.
file.close()

## Appending data to the text file, the new data in the file.
file = open("D:\PYTHON-PROJECTS\demofile\demo.txt", 'a')
file.write("This is my seventh line....\n")
file.write("This is my eight line....\n")
file.close()  # this will sometime use to save the file,after change.
print("program is completed")


