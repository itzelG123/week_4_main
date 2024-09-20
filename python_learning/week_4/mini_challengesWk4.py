# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence= "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper())

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
result="Repitition"*15
print(result)  

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998
richsentence=print("Whitecaps on the bay:A broken signboard banging,In the April wind.— Richard Wright, collected in Haiku: This Other World, 1998")
richsentence= False #this is boolean
print(richsentence)
# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
#reutrns the number of items in an object
words="electroencephalographist"
print(len(words))
#itzel Garza 
#emily H
#ejmily w
################################list###################################################sss