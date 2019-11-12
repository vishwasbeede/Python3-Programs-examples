#!/bin/usr/python3
#This program output as count of strings in given list
"""This program which explain use of While conditional loop
    and explain few list operation"""


a=[1,2,3,89,56,45,'Ganesh','Suresh','mahesh'] #Create a list


b=len(a)
print("List contains",b,"elements given below")
print(a) # Display a list
y=type(a[7])
i=0
z=0
while i!=b :
    if type(a[i])== type('Strings'):
        i=i+1
        z=z+1
        #print(i,z)
    else:
        i=i+1
print(z,"elements are of Strings")
