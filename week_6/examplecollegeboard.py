newphrase="rainstorm"
         #01234578
         #123456789
#new variable called shortphrase
#assign value by slicing
#newphrase variable by removing
#the 1st 3 charcters
#and the last 3 charcters
#1st 3 chacetrrs are "rai"
#last 3 chacters are "are"
#substirng(string,start,end)

shortphrase=newphrase[3:len(newphrase)-3]
#collegeboard version [4:len(newphrase)-6]
print(shortphrase)
#explain len(newphase-3)=0-3=6
#why does it end with 6
#bc/the last index isnt included 