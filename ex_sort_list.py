#!/bin/usr/python3
#This program output as count of strings in given list
"""This program which explain use of While conditional loop,
sort list with two types of input list"""
print("\n")
a=[1,2,3,89,56,45,'Ganesh','Suresh','mahesh'] #Create a list
a_int=[]
a_str=[]
b=len(a)
print("List contain total",b,"elements:",a,"\n") # Display a list
i=z1=z2=0
while i!=b :
    if type(a[i])== type('Strings'):
        a_str.append(a[i])
        i=i+1
        z1=z1+1
        #print(i,z)
    else:
        a_int.append(a[i])
        i=i+1
        z2=z2+1

print("It has ",z1,"Strings elements &",z2,"integers elements\n")

'''print(sorted(a_int)) #It returns sort of numbersand doesn't modify list
print(sorted(a_str))
print (a_int)
print (a_str)'''
#print (sorted(a_int))
a_str.sort() # Find the difference w,r,t output
a_int.sort()
finallist=a_int+a_str
print ("When sorted, list will be:",finallist)
