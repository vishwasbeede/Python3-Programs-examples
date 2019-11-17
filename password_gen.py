#!/usr/bin/python3
import sys
from random import choice

a="0123456789qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+|"
userName=input("Enter user name\n")
password=''
while True:
    try:
        Length=int(input("Enter password limit\n"))
        break
    except ValueError:
        print("Enter integer input and try again")
        sys.exit()

for i in range (Length):
    password=password+choice(a)
print("Generated password :"+password)

f=open("storepassword.txt","a")
f.write("    ")
f.write("\n"+userName+":")
f.write(password+"\n")
f.close()

'''f=open("storepassword.txt","r")
print(f.read())
'''

f.close()
