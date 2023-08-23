
# This is the Health Management System:

f1 = open("logharry.txt", "a")
f2 = open("logrohan.txt", "a")
f3 = open("loghammad.txt","a")
f4 = open("harryEX.txt", "a")
f5 = open("rohanEX.txt", "a")
f6 = open("hammadEX.txt", "a")
def getdata():
    import datetime
    return datetime.datetime.now()

t = getdata()

def harryfood(var):
    if var =="1":
        inp = input("What harry eat")
        f = open("logharry.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var =="2":
        f1 = open("logharry.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("you have choosen a wrong option")

def rohanfood(var):
    if var == "1":
        inp = input("what rohan eat")
        f = open("logrohan.txt", "a")
        f.write(str(t))
        f.write(":")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("logrohan.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("you have choosen a wrong option")

def hammadfood(var):
        if var == "1":
            inp = input("What hammad eat")
            f = open("loghammad.txt", "a")
            f.write(str(t))
            f.write(":")
            f.write(str(inp))
            f.write("\n")
            f.close()
        elif var == "2":
            f1= open("loghammad.txt", "rt")
            r = f1.read()
            print(r)
            f1.close()
        else:
            print("you have choosen a wrong option")

def harryexe(var):
    if var == "1":
        inp = input("What excercise haary do")
        f = open("harryEX.txt", "a")
        f.write(str(t))
        f.write(": ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("harryEX.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("you have choosen a wrong option")

def rohanexe(var):
    if var == "1":
        inp = input("What excercise Rohan do")
        f = open("rohanEX.txt", "a")
        f.write(str(t))
        f.write(":")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("rohanEX.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("you have choosen a wrong option")

def hammadexe(var):
    if var == "1":
        inp = input("What excercise Hammad do")
        f = open("hammadEX.txt", "a")
        f.write(str(t))
        f.write(":")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("hammadEX.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("you have choosen a wrong option")

print("Choose the Person\n")
print("1) Harry\n2) Rohan\n3) Hammad\n")
per = input("Enter number\n")
print("For what ?\n")
print("1) Food\n2) Exercise\n")
var1 = input("Enter number\n")
print("What do you want\n")
print("1) Log\n2) Retrive\n")
inp = input("Enter number")

if per == "1":
    if var1 == "1":
        if inp == "1" or inp == "2":
            harryfood(inp)
    elif var1 =="2":
        if inp == "1" or inp == "2":
            harryexe(inp)

elif per == "2":
    if var1 =="1":
        if inp == "1" or inp == "2":
            rohanfood(inp)
    if var1 == "2":
        if inp == "1" or inp == "2":
            rohanexe(inp)

elif per == "3":
    if var1 == "1":
        if inp == "1" or inp == "2":
            hammadfood(inp)
    if var1 == "2":
        if inp == "1" or inp == "2":
                hammadexe(inp)

else:
    print("you have choosend worng entry")

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()













