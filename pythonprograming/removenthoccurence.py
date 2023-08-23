

mylist= [1,2,3,2,4,2,5,2]
l = len(mylist)
num = 2
count = 0
for i in mylist:
    if mylist[i]==num:
        count = count+1
        if count>1:
            del mylist[i]

print(count)
print(mylist)