import pickledb
import sys
import os

db = pickledb.load("logindata.db", True)

if not db.exists("login"):
    db.set("login", input("While your castom username: "))
    db.set("password", input("While your castom password: "))
else:
    if input("While username: ") != db.get("login"):
        print("Incorect username!")
        os.system("cd && cd Termux-login && cd Core && bash exit.sh")
    if input("While password: ") != db.get("password"):
        print("Incorect password!")
        os.system("cd && cd Termux-login && cd Core && bash exit.sh")

print("\nWelcome, {}!".format(db.get("login")),
      "succesful autorized!")
