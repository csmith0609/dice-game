import json
from dice import generate_dice_roll
from auth import authenticate_users
from rule_engine import calculate_score

def main():
    # if not authenticate_users(): return

    player_1_total = 0
    player_2_total = 0
    
    for i in range(5):
        print('Round {}'.format(i + 1))
    
        dice1 = generate_dice_roll() 
        dice2 = generate_dice_roll()
        player_1_total += calculate_score(dice1, dice2)
        print(player_1_total)
        
        dice1 = generate_dice_roll() 
        dice2 = generate_dice_roll()
        player_2_total += calculate_score(dice1, dice2)
        print(player_2_total)
    
    print(player_1_total)
    print(player_2_total)
    if player_1_total > player_2_total:
        print("Player 1 is the winner!!")
    else:
        print("Player 2 is the winner!!!")
     

    return True
    
if __name__ == '__main__':
    main()
