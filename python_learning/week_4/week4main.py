# #############################complete slide 1 challenge from week 4 slideshow##########
# #############################20 minutes################################################

# ##########################Reviewing somethings

# # indexing strings -- slide 4
# my_text = 'this is a text '
# result = my_text  #get the index of the letter a
# print(result[5:7])
# print(result[0:4])#print the 1st 4 letters
# print(result[-1]) #print the last lerter of the text
# #this is called indexing\
# #index slicing is a way to get a substrong from a string
# #print the last letter of the text
# print(result[-1])
# #get the index of the third letter from the end of the text
# print(result[-3])
# # find the index of the letter s
# print(result.find('s'))
# print(result.find('text'))
# pepRally="Hancock college prep cheerleaders are the best"#prints out -1 bc/cheerleaders in not in string 
# #find index of word cheerleaders in string
# print(pepRally.find("cheerleaders"))
# print(pepRally[21:32])
# ###slide 5
# # string[start:stop:step]
# #example
# text = "Hello, World!"
# print(text[0:12:3])  # prints "World"
# text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # Get the substring CDE and put in a variable
# print(text.find('C'))
# print(text.find('E'))
# #use index to find substring
# print(text[2:5])
# #get the first letter all the way to the 4th letter
# print(text[0:4])
# #get the first letter to the final letter and skip every 3rd letter
# print(text[0:-1:3])
# # Built-in methods:
# # Python has a variety of built-in methods to work with substrings.

# # a. str.find():
# # This method returns the lowest index of the substring if found in the given string. If it's not found, it returns -1.
# # text = "Hello, World!"
# # print(text.find("World"))  # prints 7
# # print(text.find("Earth"))  # prints -1

# #################################Extracting Sub-Strings###################################
# # Extracting Sub-Strings Practice #1
# # Extract the first word of the following sentence using slicing, and display it on the screen:
# text2="Controlling complexity is the essence of programming"
# print(text2[0:12])
# # Hint: "Controlling" is 11 characters long.

# # Extracting Sub-Strings Practice #2
# # Take every third character starting from the ninth to the end of the sentence, and print the result.
# practice2="Never trust a computer you can't throw out a window"
# print(practice2[9:-1:3])

# # Extracting Sub-Strings Practice #3
# # Reverses the position of all the characters in the following sentence and displays the result on the screen.
# Practice3="It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
# print(Practice3[::-1])
##################################### String Methods#################################
#uppercase method in python
sentence= "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper()) #prints the sentence in uppercase
print(sentence.find("communications"))#prints out index of the word
#uppercase the word "communications" in the sentence
print(sentence.replace("communications","COMMUNICATIONS"))#PRINTS WORD COMMUNICATION IN UPPERCASE
#string slicing
print(sentence[26:39].upper())
print(sentence.replace("electronic","ELECTRONIC"))
print(sentence.replace("communications","communications".upper()))

#lowercase method
sentence2="ESPEN IS THE BEST SPORTS NETWORK"
print(sentence2.lower())#print sentence in lowercase




# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]

# String Methods Practice #3
# Replace in the following sentence:
sentence3="If the implementation is hard to explain, it might be a bad idea."
print(sentence3.replace("hard","easy"))
print(sentence3.replace("bad","good"))
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.
# print((modifiedsentence=sentence3.replace.("hard","easy")).replace("bad","good"))

# #join method
word_list=["simple","is","better","than","complex."]
print(word_list)
joined_sentence =" ".join(word_list)
print(joined_sentence)

new_word_list=["apples","bannas","mango","cherry","watermelon."]
joined_sentence2 ="💕💕".join(new_word_list) #window semicolon
print(joined_sentence2)

#split method
sentence4= "I am a python programmer"
print(sentence4.split())#splits the sentence into a list of words
#prints out as['I'.'am','a','python','programmer']

#this method splits sentence by comma
print(sentence4.split(","))#splits sentence into a list of words using seperators
#prints out as ['I am a programmer']

print(sentence4.split("a"))#splits sentence into a list of words using seperatores
#takes out a
print(sentence4.split("p"))

#concatnation with words in python reptition 15 times
result="Repitition"*15
print(result)

#1st paragraph of declartion 
#place in in fisrt_paragraph
#replace word people with citizens 
#print
#remove all space and replace commas with empjid
first_paragraph="The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
print(first_paragraph.replace(" ","💕"))
print(first_paragraph.replace("people ","citizens"))
#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.

################################list###################################################
# Lists Practice #1
# Print the following list on the screen:
# ["Python", "is", "easy", "to", "learn"]

# Lists Practice #1
# Create a list with 5 elements, inside the variable my_list. You can include strings, booleans, numbers, etc.

# Lists Practice #2
# Add the element "motorcycle" to the following list of means of transportation:
# transportation_means = ["plane", "car", "ship", "bicycle"]
# You must not modify the already supplied line of code, but must use the appropriate list method to add a new element.

# Lists Practice #3
# Use the pop() method to remove the third item from the following list called fruits, and store it in a variable called deleted_item. Use list methods without altering the line of code already supplied.
# apple
# banana
# mango
# cherry
# watermelon

#######################################Dictionaries###############################
# Dictionaries Practice #1
# Create a dictionary called fruits with the following key-value pairs:
# apple --> red
# banana --> yellow
# mango --> green
# cherry --> red
# watermelon --> green
# Display the dictionary on the screen.

# Dictionaries Practice #1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist
# The names of the keys and values must be equal to the ones indicated above.

#   Dictionaries Practice #2
# Use print to returns the second item of the list called points2, inside the following dictionary.
# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
# my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
# print(my_dict[]) #Use dictionary indices to extract the second item of points2

# Dictionaries Practice #3
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
# name: Karen
# surname: Jurgens
# age: 36
# occupation: Editor
# country: Colombia
# to do this, you should not change the line of code already written, but update the values using dictionary methods.
# my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}

################################Tuples##################################

# Tuples Practice #1
# Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:

# my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

# Tuples Practice #2
# Convert the following tuple to a list, and store it in a variable called my_list.

# my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)

# Tuples Practice #3
# Extract the elements of the following tuple into four variables: a, b, c, d

# my_tuple = (1, 2, 3, 4)

###############################SETS########################################
# Sets Practice #1
# Join the following sets into one, called my_set_3:
# {1, 2, "three", "four"}
# {"three", 4, 5}
# my_set_1 = {1, 2, "three", "four"}

# my_set_2 = {"three", 4, 5}

# Sets Practice #2
# Remove a random item from the following set, using set methods.
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}

# Sets Practice #3
# Add the name Gunther to the following set, using set methods:
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}

###########################Booleans#######################################

# Booleans Practice #1
# Make a comparison that returns a boolean and store the result (True/False) in a variable called test

# Booleans Practice #2
# Check if 17834/34 is greater than 87*56 and print the boolean result to the screen using print()

# Booleans Practice #3
# Check if the square root of 25 is equal to 5 and display the result (boolean) on the screen using print()

###############################Proceed to last slide#################################