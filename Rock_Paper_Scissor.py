import random
import time

print("Welcokme in game of #Rock, #Paper, #Scissor...\n\nMy name is TRINETRA and i am your competeter")

name=input("\nWhat's your name : ")

print("\n\n       let's play it now...!!!")

print("\nEnter \n\t 1 for #Rock\n\t 2 for #Paper \n\t 3 for #Scissor -->>>")
user_choice=int(input())

if user_choice in [1,2,3]:
    
    print("\n How many time you want to compete :))) \n")
    num_iter=int(input())

    list=["Rock","Paper","Scissor"]

    won=0
    lose=0
    tie=0

    #com_choice=random.choice(list)
    print("\n>>>")

    t0=time.time()

    for i in range(num_iter):
        com_choice=random.choice(list)
        if user_choice==1:
            print("Rock" + " Vs " + str(com_choice))
            if com_choice==list[0]:
                tie+=1
                print("So, There is Tie over here \n")
            elif com_choice==list[2]:
                won+=1
                print("So, You won against computer. Yahhh!!! \n\n\t *^_^* *^_^* *^_^* ")
            elif com_choice==list[1]:
                lose+=1
                print("So, You lose this game, Better luck next time... \n\n\t {{{>_<}}} {{{>_<}}} {{{>_<}}}")
            else :
                print("plz give valid input...!!!")

        elif user_choice==2:
            print("Paper" + " Vs " + str(com_choice))
            if com_choice==list[1]:
                tie+=1
                print("So, There is Tie over here \n")
            elif com_choice==list[0]:
                won+=1
                print("So, You won against computer. Yahhh!!! \n\n\t *^_^* *^_^* *^_^* ")
            elif com_choice==list[2]:
                lose+=1
                print("So, You lose this game, Better luck next time... \n\n\t {{{>_<}}} {{{>_<}}} {{{>_<}}}")
            else :
                print("plz give valid input...!!!")

        elif user_choice==3:
            print(("Scissor") + " Vs " + str(com_choice))
            if com_choice==list[2]:
                tie+=1
                print("So, There is Tie over here \n")
            elif com_choice==list[1]:
                won+=1
                print("So, You won against computer. Yahhh!!! \n\n\t *^_^* *^_^* *^_^* ")
            elif com_choice==list[0]:
                lose+=1
                print("So, You lose this game, Better luck next time... \n\n\t {{{>_<}}} {{{>_<}}} {{{>_<}}}")
            else :
                print("plz give valid input...!!!")
        else :
            print("plz enter valid input")
            print("\n")

    print("SCORES are Here : \n>>>")
    print("Winning Matches by",name,":    ",won)
    print("Winnning Matches by TRINETRA :",lose)
    print("Tie Matches :                 ",tie,"\n\n")

    if won>lose :
        print("Finally, the match is won by",name)
    elif won<lose:
        print("Finally, the match is won by TRINETRA")
    else :
        print("Finally, the match is DRAW")

    t1=time.time()
    print("\nTime taken to play this game : ",t1-t0)
    
else:
    print("Plz Enter valid input in game...!!!")
       

