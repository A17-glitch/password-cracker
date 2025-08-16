from random import *
import os
import string

u_pwd = input("Enter a password: ")

# Fill pwd with possible characters
pwd = list(string.ascii_letters + string.digits + string.punctuation + " ")


pw = ""
while(pw!=u_pwd):
    pw=""
    for latter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd)-1)] # pick random character
        pw = str(guess_pwd) + str(pw) # keep your original order
        print(pw)
        print("Cracking Password...Please Wait!")
        os.system("cls" if os.name == "nt" else "clear") # cross-platform clear

print("Your Password is: ",pw)