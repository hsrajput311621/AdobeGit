# Mini Project to write the text in the file for the future and view the file.
from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# def load_key():
#      file = open("key.key", "rb")
#      key = file.read()
#      file.close()
#      return key

def add():
    name = input("Account Name")
    pwd = input("Enter Password")
    with open('password.txt', 'a') as f:
        f.write(name + ":" + pwd + "\n")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(":")
            print("User:", user, "| Password: ",passw)


while True:
    master_pwd = input("Enter the master password to use the file content ").lower()
    if master_pwd == "text":
        print("Welcome to the data world")
    else:
        print("Wrong password! Authorize Failed")
        break
    mode = input("Which of the mode you want to select, view|add ? ")
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Wrong selection, please select correct option")


