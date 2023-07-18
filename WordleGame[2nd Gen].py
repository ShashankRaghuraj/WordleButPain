import random
import sys
from termcolor import colored
import colorama
from colorama import Fore
import nltk
nltk.download("words.txt")
from nltk.corpus import words

print("\n")
print("__          __           _ _        _ ")
print("\ \        / /          | | |      | |")
print(" \ \  /\  / /__  _ __ __| | | ___  | |")
print("  \ \/  \/ / _ \| '__/ _` | |/ _ \ | |")
print("   \  /\  / (_) | | | (_| | |  __/ |_|")
print("    \/  \/ \___/|_|  \__,_|_|\___| (_)")
                                       
                                       
                                       
                                       
print("\n")               


counter = 0
backCounter = -1
wordsUsed = ["","","","","",""]

rows, cols = (6,5)
wordleBoard = [["" for i in range(cols)] for j in range(rows)]
 
status = [["" for i in range(cols)] for j in range(rows)]

for i in range(len(wordleBoard)):
    for j in range(len(wordleBoard[i])):
        wordleBoard[i][j] = " _ "



def print_menu():
    print("Enter a 5 letter word")

nltk.data.path.append("words.txt")

wordList = words.words()
#splits up the word
words_five = [word for word in wordList if len(word) == 5]
#print(len(words_five))
print_menu()

play_again = ""
while play_again != "y":
    #makes it lower case
    word = random.choice(words_five).lower()
    for attempt in range(1, 7):
        guess = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        if wordsUsed[backCounter] == guess:
                print("You've already guessed this word. Try again")
        else:
            for i in range( min(len(guess), 5) ):
                #right, right place
                    wordsUsed[counter] = guess
                    if guess[i] == word[i]:
                        #print(colored(guess[i], 'green'), end=" ")
                        wordleBoard[counter][i] = "\x1b[92m " + guess[i] + " "
                        status[counter][i] = 0
                    #right, wrong place
                    elif guess[i] in word:
                        #print(colored(guess[i], 'yellow'), end=" ")
                        wordleBoard[counter][i] = "\x1b[93m " + guess[i] + " "
                        status[counter][i] = 1
                    #wrong
                    else:
                        #print(guess[i], end=" ")
                        wordleBoard[counter][i] = "\x1b[37m " + guess[i] + " "
                        status[counter][i] = 2

        print()
        counter+=1
        backCounter+=1
        #got it right
        if guess == word:
            print(colored(f"Congrats you got the word in {attempt}", 'blue'))
            break
        elif attempt == 6:
            print(f"You're ass, the word was {word}")
        for i in range(len(wordleBoard)):
            print("")
            for j in range(len(wordleBoard[i])):
                line = ""
                if("\x1b[92m" in wordleBoard[i][j]):
                    print(Fore.GREEN + " " + wordleBoard[i][j] + " ", end = '')
                elif("\x1b[91m" in wordleBoard[i][j]):
                    print(Fore.RED + " " + wordleBoard[i][j] + " ", end = '')
                elif("\x1b[93m" in wordleBoard[i][j]):
                    print(Fore.YELLOW + " " + wordleBoard[i][j] + " ", end = '')
                else:
                    print(Fore.WHITE + " " + wordleBoard[i][j] + " ", end = '')
        print("\n")
    play_again = input(Fore.WHITE + "Type y to play again")