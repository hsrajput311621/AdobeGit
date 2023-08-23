# for loop with Range()#
# a=int(input("Enter the value of for loop"))

#for n in range(a):
 #   print(n)

#for k in range(1, a):
 #   print(k)

#for x in range(2,a,2):
#    print(x)

# for i in range(1,11):
#     o=a*i
#     print(o)

# l1=['orange','black','white']
# l2=['chair','book','laptop']
# for i in l1:
#      for j in l2:
#          print(i,j)

# n=int(input("please enter the value of pyramid"))
# for i in range(n):
#     for j in range(i):
#         print("*",end="")
#     print("\r")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("\r")
# a=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a=a+1
#     print("\r")

a=100
n=1
while(n<=5):
    if(n<4):
        print(a-n)
    else:
        print(a+n)
    n=n+1