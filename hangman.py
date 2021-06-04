import os

def createEmptyWord(word):
    emptyWord = ""
    for i in range(len(word)):
        emptyWord += "_"
    return emptyWord    

def updateFoundLetters(word, letter, found):
    myword = list(found)
    for i in range(len(word)):
        if word[i] == letter:
            myword[i] = letter
    return "".join(myword)        

def printFound(found):
    for i in found:
        print(i, end =" ")
    print("")     


HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ===''']


turn = 1
wrong = 0
word = input("player "+ str(turn) +" please enter the word ")
turn = 2
clear = lambda: os.system('cls')
clear()
found = False
foundLetters = createEmptyWord(word)

while(found == False):
    print("\n")
    printFound(foundLetters)
    letter = input(" \n player "+ str(turn) +" please enter a letter ")
    if (letter in foundLetters) or (letter not in word):
        if wrong < len(HANGMAN_PICS)-1:
            wrong += 1
        else:
            print("player "+str(turn)+" lost. maybe next time")
            found = True

    elif letter in word:
        foundLetters = updateFoundLetters(word, letter, foundLetters)           
    
    if found == False:
        print(HANGMAN_PICS[wrong])
        if not "_" in foundLetters:
            found = True
            print("player "+str(turn)+" won well done")






