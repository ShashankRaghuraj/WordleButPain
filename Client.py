import random
import sys
from termcolor import colored
import colorama
from colorama import Fore
import nltk
import socket
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

host = '192.168.1.16'
port = 21568
              


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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
    punishment = 1
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
                        punishment+=0.05
                    #wrong
                    else:
                        #print(guess[i], end=" ")
                        wordleBoard[counter][i] = "\x1b[37m " + guess[i] + " "
                        status[counter][i] = 2
                        punishment+=0.1

        print()
        counter+=1
        backCounter+=1

        #got it right
        if guess == word:
            print(colored(f"Congrats you got the word in {attempt}", 'blue'))
            break

        #six attempts
        elif attempt == 6:
            print(f"You're ass, the word was {word}")
            break

        #print with colors
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
        #pain...
        s.send(str.encode(str(punishment)))
        reply = s.recv(1024)
        print(" \n\n"+reply.decode('utf-8'))
        print("\n")
    break
s.close()



# while True:
#     command = input("Enter your command: ")
#     if command == 'EXIT':
#         s.send(str.encode(command))
#         break
#     elif command == 'KILL':
#         s.send(str.encode(command))
#         break
    # s.send(str.encode(command))
    # reply = s.recv(1024)
    # print(reply.decode('utf-8'))
# s.close()