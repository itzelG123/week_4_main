#while loops =execute some code WHILE some conditons remain true 
#while loops an for loops 
#are forms of iteration
#iteration is the process of 
#repareting or looping through
#s aet of instuctions
#to iterate is the verb
#form of iteration
#be cxraeful of infinte loops
#they will crash your program
#and you will have to restart it 
#inifinte loops are loops that never end 

#######################WHILE LO{}ops ######################

# name =input("enter your name")
# while name=="":
#         print("ypu did not enter your name")
#         name=input("enter your name")

#         print(f"hello{name}")
#  #crtl c to stop infite loop
# i=#inifte loop 


# age=int(input("enter your age")):

# while age <0:
#         print("age cant be negitive")
#         age=int(input("enter your age :"))
#         #if remove this =infinite 
#         print(f"you are {age}years old")


#3 food =input("enter a food you like(q to quit):")

# while not food == "q":
#     print(f"you like {food}")
#     food=input("enter another food ytou like(q to quit)")

# print("bye") 

#4
# num =int(input("enter a num 1-10"))

# while num <1 or num > 10 :
#     print(f"{num}is not valid")
#     num =int(input("enter a num between 1-10 "))

# print(f"your number is {num}")




#####################################for loops
#for loops = execute a block of code a fixed number of times
#you can iterate over a range string sequnce etc
#iterate go through list

# for x in range(1,11):#last number is exclusive
#     print(x)
#     #this is a list goes through list of items
# print("happy new year")



# for x in reversed(range(1,11)):#reverses
#     print(x)
#     #this is a list goes through list of items
# print("happy new year")


# for x in range(1,11,3):#skipes by 3 
#     print(x)
#     #this is a list goes through list of items


# credit="1234-5678-9012-3456"

# for x in credit:
#     print(x)  



# for x in range(1,21):
#     if x == 13:
#         continue #skips over it 
#     else:
#         print(x)


# for x in range(1,21):
#     if x == 13 or x==15 or x==19:
#         continue #skips over it 
#     else:
#         print(x)


# for x in range(1,21):
#     if x == 13 or x==15 or x==19:
#        break #stops program at 13 
#     else:
#         print(x)



############################# CHALLENGE ######################################
horror_movie =['exprcist','the shining','conjuring','the ring']

#loop though list
#if the name is the shining print the shining
#otherwise print the shinging [rint the shining]
#otherwise print the shining was not found and print
#ouy yhr oyhrt names using a loop 

 for movies in horror_movie:
    if movies == 'the shining':
       print("the shining")
        print(movies)
   else:
        print("the shining")
         print(movies)


#2 create a list of your favorite horror movie chracters 
# loop through the list of chracters
# if the name is "Freddy Krueger", skip over it
# otherwise, print out the name of the chracter

horror_charcters=["scream",'terrifer','it','megan','freddy kruger']

for charcters in horror_charcters:
    if charcters == 'it':
       continue #skips over it 
    else:
       print(charcters)


#3 create a list of yout favorite horror movie monsters
# loop through the list of names
# if the name is for example "swamp thing", replace it with another name

