import random
cnum = random.randrange(1,50)
#print(cnum)
usernum = int(input("Enter the random number between 1 to 50 to win from the computer"))
print(usernum)
if usernum>cnum:
    print(cnum)
    print("You defeated the computer")
elif cnum>usernum:
    print(cnum)
    print("Computer is too far from you")
else:
    print(cnum)
    print("you both are at the same place")
