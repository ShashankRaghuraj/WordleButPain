from os import dup
from pickle import FALSE
import random
import colorama
from colorama import Fore

wordleWord = ""
rowCounter = 0
wordleWordDuplicates = []
guessWordDuplicates = []
duplicateCount = []
guessDuplicateCount = []

def split(word):
    return [char for char in word]
def checkDuplicates(string, duplicates):
    for char in string:
        if string.count(char) > 1:
            ## appending to the list if it's already not present
            if char not in duplicates:
                duplicates.append(char)
                duplicateCount.append(string.count(char))
    print(duplicates)
print(duplicateCount)

print("\n")
print(" _       __                  __ __         ____          __     ____          _")      
print("| |     / /____   _____ ____/ // /___     / __ ) __  __ / /_   / __ \ ____ _ (_)____") 
print("| | /| / // __ \ / ___// __  // // _ \   / __  |/ / / // __/  / /_/ // __ `// // __ \\")
print("| |/ |/ // /_/ // /   / /_/ // //  __/  / /_/ // /_/ // /_   / ____// /_/ // // / / /")
print("|__/|__/ \____//_/    \__,_//_/ \___/  /_____/ \__,_/ \__/  /_/     \__,_//_//_/ /_/ ")
print("")               


# Open the file in read mode
with open("Words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
    wordleWord = random.choice(words)
    wordleWordArray = split(wordleWord)
    print(wordleWord)
checkDuplicates(wordleWord, wordleWordDuplicates)
if not duplicateCount:
    duplicateCount = [0]
print(duplicateCount)
wordsGuessed = ["","","","","",""]
rows, cols = (6,5)
arr = [["" for i in range(cols)] for j in range(rows)]
 
status = [["" for i in range(cols)] for j in range(rows)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = " _ "

# for rows in arr:
#     print(rows)
timesGuessed = 0
while True:
    guess = input("Enter word: ") #ask for word
    guess = guess.lower() #make it lower case for case sensitivity
    isWord = FALSE #need to check if the word is an actual word
    #reads file to see if it is a word
    with open('Words.txt') as file:
        contents = file.read()
        if guess in contents:
            isWord = True
        else:
           isWord = False
    #word can't be more than 5 letters, or less than 5 letters and it also has to be word
    if(len(split(guess)) > 5 or len(split(guess)) < 5 or isWord == False or wordsGuessed[timesGuessed] == guess):
        print("Not Valid. Guess again")
    else:
        checkDuplicates(guess, guessWordDuplicates)
        timesGuessed +=1
        wordsGuessed[timesGuessed] = guess
        iterator = 0 #iterator
        iterator2 = 0
        counter = 0
        if(guess == "EXIT"):
            break
        else:
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if(i == rowCounter): 
                        for k in range(len(wordleWordArray)):

                            if(list(guess)[iterator] in wordleWordArray):
                                arr[i][counter] = "\x1b[93m " + list(guess)[iterator] + " "
                                status[i][counter] = 1
                            if(list(guess)[iterator] == wordleWordArray[k]):
                                arr[i][counter] = "\x1b[92m " + list(guess)[iterator] + " "
                                status[i][counter] = 0
                            if(list(guess)[iterator] not in wordleWordArray):
                                arr[i][counter] = "\x1b[37m " + list(guess)[iterator] + " "
                                status[i][counter] = 2

                            if(iterator >= len(wordleWord)-1):
                                break
                            else:
                                counter+=1
                                iterator+=1
                    else:
                        if(arr[i][j] == " _ "):
                            arr[i][j] = " _ "
            

            if(list(guess)[4] == wordleWordArray[4]):
                arr[timesGuessed-1][4] = "\x1b[92m " + list(guess)[4] + " "
                status[timesGuessed-1][counter] = 0
            elif(list(guess)[4] in wordleWordArray ):
                arr[timesGuessed-1][4] = "\x1b[93m " + list(guess)[4] + " "
                status[timesGuessed-1][counter] = 1
            else:
                arr[timesGuessed-1][4] = "\x1b[37m " + list(guess)[4] + " "
                status[timesGuessed-1][counter] = 2
            
            charUsed = 0
            charHighlightOnce = 0
            # check for duplicates


            for i in range(len(arr)):
                print("")
                for j in range(len(arr[i])):
                    line = ""
                    if("\x1b[92m" in arr[i][j]):
                        print(Fore.GREEN + " " + arr[i][j] + " ", end = '')
                    elif("\x1b[91m" in arr[i][j]):
                        print(Fore.RED + " " + arr[i][j] + " ", end = '')
                    elif("\x1b[93m" in arr[i][j]):
                        print(Fore.YELLOW + " " + arr[i][j] + " ", end = '')
                    else:
                        print(Fore.WHITE + " " + arr[i][j] + " ", end = '')
                    
            if(guess == wordleWord):
                print("\nCongrats you got the word in " + str(timesGuessed) + " tries")
                break
            print("\n")

            if(timesGuessed == 6):
                print(Fore.RED + "You Lost")
                print("The word was " + wordleWord)
                break

            rowCounter +=1