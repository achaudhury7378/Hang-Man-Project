import random as r
import os
def Draw_Man(n,Draw):
    if n==0:
        for i in Draw:
            print(i)
    elif n==1:
        Draw[3]="   O    |"
        Draw_Man(0,Draw)
    elif n==2:
        Draw[4]="   |    |"
        Draw_Man(1,Draw)
    elif n==3:
        Draw[4]="  \|    |"
        Draw_Man(1,Draw)
    elif n==4:
        Draw[4]="  \|/   |"
        Draw_Man(1,Draw)
    elif n==5:
        Draw[5]="   |    |"
        Draw_Man(4,Draw)
    elif n==6:
        Draw[6]="   |    |"
        Draw_Man(5,Draw)
    elif n==7:
        Draw[7]="  /     |"
        Draw_Man(6,Draw)
    elif n==8:
        Draw[7]="  / \   |"
        Draw_Man(6,Draw)
Draw=["   ______","   |    |","   |    |","        |","        |","        |","        |","        |","________|"]
print("Hey Welcome to Hang-Man ")
print("Press 1 for playing with computer")
print("Press 2 for playing with another person player 2")
chance=0
choice=int(input())
if choice ==1 :
    print("Computer will choose a word and you have to guess it within 8 lifes")
    words = '''ant baboon badger bat bear beaver camel cat clam computer cobra cougar coyote
            crow deer dog donkey district duck eagle ferret fox frog goat goose hawk lion laptop lizard llama
            mole monkey moose mouse moble magistrate monitor mule newt otter owl panda phone police power parrot pigeon python rabbit
            rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
            toad trout turkey turtle weasel whale wolf wombat zebra zipper'''.split()
    word=r.choice(words)
    guess_progress=["-" for i in range(len(word))]
    guess=""
    while True :
        s=""
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    guess_progress[i]=word[i]
            print("Word is ",end="")
            for k in guess_progress:
                print(k,end="")
            print("\n")
        else:
            chance=chance+1
            print("Word is ",end="")
            for k in guess_progress:
                print(k,end="")
            print("\n")
        Draw_Man(chance,Draw)
        if chance==8:
            print("You loose.....stop trying")
            print("The word was",word)
            break
        for k in guess_progress:
            s=s+k
        if s==word:
            print("You won the game")
            break
        print("You have got ",8-chance,"lifes")
        guess=input("Input your guess letter")
elif choice==2:
    print("Player 1 will choose a word and you have to guess it within 8 lifes")
    word=input("The secret word(lower cases) ")
    os.system('cls')
    guess_progress=["-" for i in range(len(word))]
    guess=""
    while True :
        s=""
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    guess_progress[i]=word[i]
            print("Word is ",end="")
            for k in guess_progress:
                print(k,end="")
            print("\n")
        else:
            chance=chance+1
            print("Word is ",end="")
            for k in guess_progress:
                print(k,end="")
            print("\n")
        Draw_Man(chance,Draw)
        if chance==8:
            print("You loose.....stop trying")
            print("The word was",word)
            break
        for k in guess_progress:
            s=s+k
        if s==word:
            print("You won the game")
            break
        print("You have got ",8-chance,"lifes")
        guess=input("Input your guess letter")
print(Draw)

        


    
            
            
        