print("Welcome to my computer Quiz")

playing = input("Do you want to play ")
if playing.lower() != "yes":
    quit()

print("Great! Let's play the game")
score = 0

answer = input("What is the CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score +=1
else:
    print("Sorry, Incorrect Answer")

answer = input("What is the GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Sorry, Incorrect Answer")
answer = input("What is the RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Sorry, Incorrect Answer")
answer = input("What is the ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Sorry, Incorrect Answer")

print("You got " + str(score)+ " questions correct!")
print("You got " + str((score/4)*100)+"%")

