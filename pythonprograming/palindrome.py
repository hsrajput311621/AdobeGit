
str = input("Please enter the string")

str1 = str[::-1]

if str == str1:
    print("String is palindrome")
else:
    print("Not palindrome")


# reverse the words in the string or the sentence

str = input("Enter the sentence")
words = str.split(" ")
print("before reverse", words)
words = words[::-1]
print("after reverse", words)
outputstr = ' '.join(words)
print(outputstr)

