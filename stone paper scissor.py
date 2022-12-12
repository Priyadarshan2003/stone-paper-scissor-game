# coded by PRIYADARSHAN N S
# project: stone paper scissor game

from random import randint

def name(c):
    if c==1:
        player=input("\nType your name: ")
        return player
    else:
        players=["elem1","elem2"]
        players[0]=input("\nType name of player 1: ")
        players[1]=input("Type name of player 2: ")
        return players
    
def play(c,player):
    lst=["stone", "paper", "scissor"]
    score1=0
    score2=0
    if c==1:
        a=1
        while(a==1):
            print("\n1. stone\n2. paper\n3. scissor")
            playerchoice=int(input("Enter your choice [1/2/3]: "))
            compchoice=randint(1,3)
            print("Computer chose: ",lst[compchoice-1])
            print("You chose: ",lst[playerchoice-1])
            if playerchoice==compchoice:
                print("It is a tie")
            elif playerchoice>compchoice:
                if playerchoice==3 and compchoice==1:
                    print("Computer won")
                    score2+=1
                else:
                    print("You won")
                    score1+=1
            else:
                if playerchoice==1 and compchoice==3:
                    print("You won")
                    score1+=1
                else:
                    print("Computer won")
                    score2+=1            
            a=int(input("Do you wish to continue? (yes-->1 , no-->2): "))    
            if a==2:
                print("Your score = ",score1)
                print("Computer score = ",score2)
                if score1>score2:
                    print("Congratulations",player,", you won")
                elif score2>score1:
                    print("Better luck next time")
                else:
                    print("It is a tie")
    else:
        a=1
        player1=player[0]
        player2=player[1]
        while(a==1):
            print("\n1. stone\n2. paper\n3. scissor")
            player1choice=int(input("{} Enter your choice [1/2/3]: ".format(player1)))
            player2choice=int(input("{} Enter your choice [1/2/3]: ".format(player2)))
            print(player1,"chose: ",lst[player1choice-1])
            print(player2,"chose: ",lst[player2choice-1])
            if player1choice==player2choice:
                print("It is a tie")
            elif player1choice>player2choice:
                if player1choice==3 and player2choice==1:
                    print(player2," won")
                    score2+=1
                else:
                    print(player1," won")
                    score1+=1
            else:
                if player1choice==1 and player2choice==3:
                    print(player1," won")
                    score1+=1
                else:
                    print(player2," won")
                    score2+=1            
            a=int(input("Do you wish to continue? (yes-->1 , no-->2): "))    
            if a==2:
                print()
                print(player1," score = ",score1)
                print(player2," score = ",score2)
                if score1>score2:
                    print("Congratulations ",player1,", you won")
                elif score2>score1:
                    print("Congratulations ",player2,", you won")
                else:
                    print("It is a tie")
    return 0

print("Welcome to stone paper scissor!\n")

ch=int(input("(1) 1 player\n(2) 2 player\nEnter your choice[1/2]: "))
if ch!=1 and ch!=2:
    print("invalid choice")
    ch=int(input("Enter your choice[1/2]: "))
if ch==1:
    player=name(ch)
    play(ch,player)
else:
    players=name(ch)
    play(ch,players)  
    # end of code