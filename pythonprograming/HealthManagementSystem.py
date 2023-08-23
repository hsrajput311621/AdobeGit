f1 = open("logharry.txt", "a")
f2 = open("logrohan.txt", "a")
f3 = open("loghammad.txt", "a")
f4 = open("harryEx.txt", "a")
f5 = open("rohanEx.txt", "a")
f6 = open("hammadEx.txt", "a")
def getdate():
    import datetime
    return datetime.datetime.now()
t = getdate()

def harryfood(var):
    if var == "1":
        inp = input("What Harry Eat:")
        f = open("logharry.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("logharry.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def rohanfood(var):
    if var == "1":
        inp = input("What Rohan Eat:")
        f = open("logrohan.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("logrohan.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def hammadfood(var):
    if var == "1":
        inp = input("What Hammad Eat:")
        f = open("loghammad.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("loghammad.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def harryexer(var):
    if var == "1":
        inp = input("What Harry done:")
        f = open("harryEx.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("harryEx.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def rohanexer(var):
    if var == "1":
        inp = input("What Rohan done:")
        f = open("rohanEx.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("rohanEx.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def hammadexer(var):
    if var == "1":
        inp = input("What Hammd done:")
        f = open("hammadEx.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("hammadEx.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


print("Choose Persone: ")
print("1. Harry\n2. Rohan\n3. Hammad")
per = input()
print("For what ?\n")
print("1. Food\n2. Exercise")
var1 = input()
print("What do you want ?")
print("1. Log\n2. Retrive")
inp = input()

if per == "1":
    if var1 == "1":
        if inp == "1" or inp == "2":
            harryfood(inp)
    elif var1 == "2":
        if inp == "1" or inp == "2":
            harryexer(inp)

elif per == "2":
    if var1 == "1":
        if inp == "1" or inp == "2":
            rohanfood(inp)
    elif var1 == "2":
        if inp == "1" or inp == "2":
            rohanexer(inp)

elif per == "3":
    if var1 == "1":
        if inp == "1" or inp == "2":
            hammadfood(inp)
    elif var1 == "2":
        if inp == "1" or inp == "2":
            hammadexer(inp)
else:
    print("You choose something wrong, Please choose correct order ")

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()