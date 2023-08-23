#Python String Function#
# lower(), upper() title(), capitalize()

a="I am a Automation Engineer working in Adobe"
n=a.lower()
print(n)

a="I am a Automation Engineer working in Adobe"
u=a.upper()
print(u)

a="I am a Automation Engineer working in Adobe"
t=a.title()
print(t)

a="I am a Automation Engineer working in Adobe"
c=a.capitalize()
print(c)


# find(), index(), isalpha(), isdigit(), isalnum()
#find()
a="I am a Automation Engineer working in Adobe"
#print(a.find('i'))
f=a.find('i')
print(f)

a="I am a Automation Engineer working in Adobe"
#print(a.find('i',2))
f=a.find('b',2)
print(f)

#index()
a="I am a Automation Engineer working in Adobe"
#print(a.find('i'))
f=a.index('i')
print(f)

#isalpha()
a="Automation"
f=a.isalpha()
print(f)

# isdigit()
a="8271821350"
f=a.isdigit()
print(f)

#isalnum()

a="Automation123"
f=a.isalnum()
print(f)

#chr() and ord()
# Convert integer 65 to ASCII character ('A')
y=chr(65)
print(type(y),y)
#output: <class'str'>A

#Conver ASCII Unicode Character 'A' to 65
y=ord('A')
print(type(y),y)

#output<class 'int'> 65

#format() Method

txt1="Welcome to {fname} {lname}".format(fname="junle",lname="Nanital")

#numbered indexes:
txt2="Welcome to {0} {1}".format("junle","Nanital")

#empty placeholders:
txt3="Welcome to {} {}".format("junjle","Nanital")

#some imp application

txt4="Welcome {a:^10} to {b:^10}".format(a=50,b=50)
print(txt1)
print(txt2)
print(txt3)
print(txt4)
