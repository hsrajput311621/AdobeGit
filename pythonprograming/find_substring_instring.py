

str =  "Welcome to python programming"
sub_str = "python"

print(str.find(sub_str))    # 11 it showing the position of the python is started

if(str.find(sub_str) == -1):
    print("not found")
else:
    print("It is found")


str =  "Welcome to python programming"
count = 0
for i in str:
    count = count+1
print(count)

# approach 2 using while loop statement

str =  "Welcome to python programming"
count = 0
while str[count:]:
    count = count+1
print(count)
