import random
print("Welcome to the Number Gussing Game")
count = 0
playing = input("Do you want to play the Game? ")
if playing.lower() != "yes":
    quit()
print("Good! let's find who good you are in Gussing")

random_number = random.randint(0,50)
print(random_number)
while True:
    number = input("Guess the number between 1 to 50: ")

    if number.isdigit():
        number = int(number)
        if number <= 0:
            print("Please type a number larger than 0")
            quit()
    else:
        print("please type a number")
        continue

    if random_number == number:
        print("Your Guess is accurate")
        count +=1
        break

    elif random_number > number:
        print("Your guess is too small")
        count +=1
    else:
        print("Your guess is too large")
        count +=1


print("You have taken " + str(count) + " Attempts")

