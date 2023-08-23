import random

uscore = 0
cscore = 0

while True:
    choice = input("Do you want to play Rock, Paper and Scissor ")
    if choice.lower() != "yes":
        break
    comp_choice = ["rock","paper","scissor"]
    rc = random.choice(comp_choice)
    uc = input("Choose any one rock,paper and scissor ")
    if (rc == "rock") & (uc == "paper"):
        print(rc)
        print("You win the round one")
        uscore +=1
    elif (rc == "paper") & (uc == "rock"):
        print(rc)
        print("Computer wins the round one")
        cscore +=1
    elif (rc == "scissor") & (uc == "paper"):
        print(rc)
        print("Computer won the round one")
        cscore += 1
    elif (rc == "paper") & (uc == "scissor"):
        print(rc)
        print("You win the round one")
        uscore += 1
    elif (rc == "rock") & (uc == "scissor"):
        print(rc)
        print("Computer win the round one")
        cscore += 1
    elif (rc == "scissor") & (uc == "rock"):
        print(rc)
        print("You win the round one")
        uscore += 1
    else:
        print(rc)
        print("Please choose again both are same")

print("Your score is " + str(uscore))
print("Computer score is " + str(cscore))
if uscore > cscore:
    print("You have defeated computer")
else:
    print("Computer defeated you")
