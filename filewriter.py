import os.path

def checkExistence():
    #this function will check if the file already exist if it doesn't it creates the file
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

def appendNew(website,userName,password):
    # This function will append new password in the txt file
    file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

def fileviewer():
    if os.path.exists("info.txt"):
        file = open("info.txt")
        # print()
        
        print(file.read())
    else:
        print("no passwords are saved")

        