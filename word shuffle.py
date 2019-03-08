##Word Shuffling
##Jacob Fancella
import random
import time
s = input("Enter a sentance:")
words = s.split(" ")
shuffled = ''

##Method used to remove the first and last chareter to prevent them from being shuffled
def removeChar(s, i):
    return s[:i] + s[i+1:]

##Converts the word to be shuffled into an array, shuffles the positions
##of the values, and joins it back into a string to be returned
##Also verifies that the shuffled string is different from the original string
def shuffleString(s):
    startingString = s
    while(s == startingString):
        charList = list(s)
        random.shuffle(charList)
        s = ''.join(charList)
    return s

for x in range(len(words)):
    ##Checks to see if word is longer than 3 chars and can be shuffled
    if(len(words[x]) > 3):
        firstLetter = words[x][0]
        words[x] = removeChar(words[x], 0)
        lastLetter = words[x][-1]
        words[x] = removeChar(words[x], len(words[x]) - 1)
        words[x] = shuffleString(words[x])
        words[x] = firstLetter + words[x] + lastLetter

    #Adds shuffled words back into a sentance
    shuffled += words[x] + " "

##Prints shuffled sentance and waits 5 seconds before ending the program
print(shuffled)
time.sleep(5)



