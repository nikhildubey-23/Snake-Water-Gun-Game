#we use random module
import random
#printing the game name
print("Snake Water Gun!")
#number of rounds
n=int(input("Enter Number of Rounds\n"))
#setting the options
options = ['s','g','w']
#computer marks
computer_wins = 0
#user marks
user_wins = 0
#number of rounds
rounds = 1
#setting the loop till user_range
while rounds <= n:
    #user message
    print(f"Round:{rounds}\nSnake-'s'\nWater-'w'\nGun-'g'")
    #user input
    try:
        player = input("Enter your option:-")
    except:
        print("Invalid input!!!!!!!!!!")

    #checking the user input
    if player != 's' and player != 'g' and player != 'w':
        print("Invalid input , Enter the right value!")
        continue
    #computer will choice its value
    computer = random.choice(options)
    # game logic
    if computer == 's':
        if player == 'w':
            computer_wins +=1
        elif player == 'g':
            user_wins += 1
    elif computer == 'w':
        if player == 's':
            user_wins += 1
        elif player == 'g':
            computer_wins += 1
    elif computer == 'g':
        if player == 's':
            computer_wins +=1
        elif player == 'w':
            user_wins += 1
            
    # winner Announcement
    if user_wins > computer_wins:
        print("User is a winner!")
    elif computer_wins > user_wins:
        print("Computer is a winner!")
    else:
        print("Match is Draw!!\n")
    #breaking the loop
    rounds += 1   
#final Winner
if user_wins > computer_wins:
    print("User is a Final winner!")
elif computer_wins > user_wins:
    print("Computer is a Final winner!")
else:
    print("Match is Draw!!")
       
        
    
    
