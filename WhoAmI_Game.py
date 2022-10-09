from objModule import obj
import random

#For e.g. in objModule let obj[] contains total 45 items, so n will become equals to 45.
n = len(obj)

score = 0
games_won=0
games_lost=0
option = 'y'
while(option=='y' or option=='Y'):
    #Now generate a random index between 0 to n-1, to work on specific item of that list obj[].
    idx = random.randint(0,n-1)
    word = obj[idx][0]
    word_len = len(obj[idx][0])
    hint = obj[idx][1]
    chances = word_len+5     # i am giving , total chances = (5 extra + no. of letters in word to be guessed.)

    print("\n * * * * * * * * * * * * * * * * * * * * * * Guess THE WORD using Hint * * * * * * * * * * * * * * * * * * * * * *")
    print("------------------------------------ (NOTE : use only CAPITAL letters while guessing) -----------------------------------\n")
    #array of 'word' letters initially as underscore (_ _ _ ....)
    arr = []
    for x in range(0,word_len):
        arr.append('_')

    print("==> HINT : ",hint)
    print("==> GUESS this WORD : ",end="")
    for ele in arr:
        print("",ele,end="")
    print("")
    print("Total Chances available :",chances)

    #Here is the letter guessing and matching with the target word.
    #count variable: is for counting how many letters of 'word' are fetched/guessesd yet.
    #chances variable : is to give maximum no. of chances given to user to guess the word.
    count=0
    while(chances>0 and count<word_len):                 # i am giving , total chances = (5 extra + no. of letters in word to be guessed.)
        char = input("\nGuess a letter = ")

        if(char not in word):                           #if letter not present
            print("! :( This Letter didn't matched.")
        else:                                            #if letter is present.
            flag = False                               
            for i in range(0,word_len):
                if(char==word[i] and arr[i]=='_'):       #means guessed letter is presnt in actual word but yet not filled in arr[] (guessed word)
                    flag = True
                    arr[i] = char
                    print(":) This letter matched.")
                    count+=1
                    break
            if(flag==False):
                print("! :( This Letter didn't matched.")
        print("Now the Word is : ",end="")
        for ele in arr:
            print("",ele,end="")
        print("")
        chances -= 1
        print("Chances left :",chances)

    if(count==word_len):                                   #means in arr[] all the underscores '_' are now converted into respected characters of words.
        games_won += 1
        score += 100
        print("\n:) CONGRATS, You WON. Word Guessed successfully.\n")
    else:
        games_lost += 1
        print("\n!!! OOPs, You LOST the GAME. No more chances left, Guess Unsuccessful.")
        print("CORRECT WORD : ",end="")
        for ele in word:
            print("",ele,end="")
        print("\n")

    option = input("Do you want to play one more time, enter Y for YES / N for NO = ")

print("\n ------------------------------------------------------------------------------------------------------------")
print("TOTAL FINAL SCORE : ",score)
print("No. of games you WON :",games_won,"out of",games_lost+games_won)
print("--------------------------------------------------------------------------------------------------------------")


