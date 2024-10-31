#Emily H and Itzel G
#8
#Ask user is they are a student and if they reside locally
student=input("are you a student?")
age=int(input("how old are you?"))
local=input("Do you reside locally?")
#if they are a student
if student =="y":
        if age <18:
                print("eligable for free student membeship")
#if they are above the age of 18 and reside locally
elif age >= 18 and local =="y" :
        print("eligbale for discounted student membership")
#if they don't meet the standards above
else:
        print("standard membership rates apply")
#if they are older then 65 or local (if either is true)
if age > 65 or local=="y":
        print("eligable for senior or resident mebership")
else:
        print("standard membership rates apply")
       


       #14
#Ask user for their driving experience + if they had accidents in the past
sdrive=input("hpw long have you driven for?")
age=int(input("how old are you?"))
accidents=input("have you had any accidents?")
#if they are 25 + less then 2 years of experience or had an accident
if age <25:
    if sdrive <2 or accidents=="y":
     print("high premium applies")
#otherwise               
else:
    print("Standard premium applies")
    if  accidents =="y":
        print("sligly higer peruimum applies")

#if they are 25 or older + had an accident
if age >= 25 and accidents =="y" :
    print("Slighty higher premium applies")


#if they are 25 or older with no accidents
if age >= 25 or accidents=="n":
        print("Standard premium applies")