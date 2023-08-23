import random

uscore = 0
cscore = 0
options = ["rock", "paper","scissor"]
while True:
    user_input = input("Type Rock, Paper and Scissor or Q to quit ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick =="scissor":
        print("you won!")
        uscore +=1
        continue

    elif user_input == "paper" and computer_pick =="rock":
        print("you won!")
        uscore +=1
        continue

    elif user_input == "scissor" and computer_pick =="paper":
        print("you won!")
        uscore +=1
        continue
    else:
        print("you lost")
        cscore +=1
print("you won", uscore, "times.")
print("Computer won", cscore, "times.")
print("Goodbye")

