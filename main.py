import random

while True:
    Player = input(
        'Enter Your weapon: R for Rock, P for Paper, S for Scissors=>:')
    possible_selection = ['R', 'P', 'S']
    CPU = random.choice(possible_selection)
    print(f"\n Player ({Player.upper()})  : CPU ({CPU})")
    if (Player.upper() == CPU):
        print("It's a tie ")
        continue
    elif (Player.upper() == 'R' and CPU == 'S'
          or Player.upper() == 'P' and CPU == 'R'
          or Player.upper() == 'S' and CPU == 'P'):
        print(" You Win!!! Weldone Player")

    elif (Player.upper() == 'R' and CPU == 'P'
          or Player.upper() == 'P' and CPU == 'S'
          or Player.upper() == 'S' and CPU == 'R'):
        print("Oh wow CPU Win!!!")
    else:
        print("Error!!! Enter the correct letter")
        print("R,P,S")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
