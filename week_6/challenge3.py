#1 ask peice of text
userText=input("enter any text")
#2ask for 3 letters
onesletter=input("1st letter")
secondletter=input("2st letter")
threeletter=input("3st letter")

#string to lowercase
onesletter.lower()
secondletter.lower()
threeletter.lower()
userText.lower()

#string to list
listofwords=userText.split()
print(listofwords)

#print wordcount
wordcount=len(listofwords)
print(f"the word count is{wordcount}")

#invert list of words
backwardslist=list(reversed(listofwords))

#join list using spaces
print("".join(backwardslist))

#create boolean asking "if python"
word_pythoninlist=True
listofwords.find("python")

#make list into bigger list using each letter
listofletters=list(userText.lower())

#find 1st and last letter 

#print how times the letter is found 


