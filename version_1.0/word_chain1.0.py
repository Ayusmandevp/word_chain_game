#using nltk module
import nltk
import random
nltk.download('words')  # Downloading word list

from nltk.corpus import words


#Function to check valid word
def word_validity(word):
    wordAllCase=[]
    wordAllCase.append(word.lower())
    wordAllCase.append(word.capitalize())
    wordAllCase.append(word.upper())
    if any(word in englishWords for word in wordAllCase):
        playerWordList.append(word.lower())
        return word.lower()
    else:
        return 0
def word_last_first(word):
    if word[0].lower() == lastWord[-1].lower():
        return word
    else:
        return 0

    #Function to drop word
def drop_word():
    word = input("Enter your word: ").strip().lower()
    if word in playerWordList:
        print("Already used...Try another one...")
        return drop_word() 
    return word

    
#function to drop word by computer
def computer_word(word):
    last_letter = word.strip().lower()[-1]
    comWordList = [w for w in englishWordsLower if w.startswith(last_letter) and w not in computerWordList]
    
    if comWordList:
        comWord = random.choice(comWordList)
        print("Computer gave:", comWord)
        computerWordList.append(comWord)
        return comWord  # ✅ Return it!
    else:
        return None

# Get all English words as a list
englishWords = words.words()       #noun verb taken different
englishWordsLower = [el.lower() for el in englishWords]
computerWordList=[]
playerWordList=[]
lastWord=""


playerName=input("Enter Your name:")
print("Welcome",playerName,"Let's Start the game...")
totalDrop=1
while True:
    firstWord=input("Enter a Word to begin the game:")
    #To find any case word is present
    firstWordCase=[]
    firstWordCase.append(firstWord.lower())
    firstWordCase.append(firstWord.capitalize())
    firstWordCase.append(firstWord.upper())
    if any(word in englishWords for word in firstWordCase):
        print("Nice Word...Let's Compete...")
        playerWordList.append(firstWord)
        lastWord=firstWord.lower()
        break
    else:
        print("Probably not a word...Please Try again")                      #first time excuse only
while True:
    lastWord=computer_word(lastWord)
    playerWord=drop_word()
    validity1=word_last_first(playerWord)
    validity2=word_validity(playerWord)
    lastWord=playerWord
    if validity1==0 or validity2==0:
        print("Game over...")
        break
    else:
        totalDrop+=1
print("You gave",totalDrop,"words")
print("Your words are",playerWordList)
print("Computer's words are",computerWordList)
