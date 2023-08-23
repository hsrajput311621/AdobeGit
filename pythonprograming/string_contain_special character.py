
import re

str =  "Welcome$ to% python^ &programming*"
regex = re.compile('[$%^&* ]')

if regex.search(str) ==None:
    print("No special characters present in a string")
else:
    print("string contain special")

    

