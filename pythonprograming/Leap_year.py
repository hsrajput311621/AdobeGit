# A leap year is exactly divisible by 4 except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400. For example,

year = int(input("Enter the year to check the leap year"))

if (year % 4) ==0:
    if (year % 400) ==0:
        print("year is a leap year")
    else:
        print("year is not a leap year")

