#a=int(input("Enter the number"))
#if a%2==0:
#    print(a, "Even number")
#else:
#    print(a, "Number is odd")

a=int(input("Enter the percentage"))
if a>75:
    print(a, "The stundent is gold medalist")
elif a>50:
    print(a, "The student is good")
elif a>30:
    print(a, "The student is average")
else:
    print("Fail")


a=int(input("Enter the first value"))
b=int(input("Enter the second value"))
c=int(input("Enter the third value"))
if (a>b) & (a>c):
    print("a is greatest")
elif (b>a) & (b>c):
    print("b is greatest")
else:
    print("c is greatest")

# if with tuple#####

# a = ('hell0', 'b', 100)
# if 999 in a:
#     print("yes 99 is present in tuple")
# else:
#     print("not present")

## if loop with list##
# a=[26,'z',"Hello",99.9]
# if a[0]==26:
#     a[0]=100
#     print(a)
# else:
#     print("we are failed to guess the number")

## if loop with dictonary##
d={
  'name':'Hitesh-Rajput',
  'age':30,
  'sex':'male',
   'salary':10000,
    'company': 'adobe'
}
print(d)
if d['age']==30:
    d['salary']=15000
    print(d)
else:
    print("there is not element like this")



