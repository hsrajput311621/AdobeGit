import random

l=["Rock", "Paper", "Scissor"]
rc = random.choice(l)
uc = input("Enter your choice out of 'Rock', 'Paper' and 'Scissor' to defeat the computer")
if (rc == "Rock") & (uc == "Paper"):
    print(rc)
    print("You win the round one")
elif (rc == "Paper") & (uc =="Rock"):
    print(rc)
    print("Computer wins the round one")
elif (rc =="Scissor") & (uc =="Paper"):
    print(rc)
    print("Computer won the round one")
elif (rc == "Paper") & (uc == "Scissor"):
    print(rc)
    print("You win the round one")
elif (rc == "Rock") & (uc =="Scissor"):
    print(rc)
    print("Computer win the round one")
elif (rc == "Scissor") & (uc == "Rock"):
    print(rc)
    print("You win the round one")
else:
    print(rc)
    print("Please choose again both are same")



