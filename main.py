import json
from dice import generate_dice_roll
from auth import authenticate_users
from rule_engine import calculate_score

def determine_winner(player_1_total, player_2_total):
    print("Tiebreak!")
    while player_1_total == player_2_total:
            player_1_total = generate_dice_roll()
            player_2_total = generate_dice_roll()

    if player_1_total > player_2_total:
            print("Player 1 is the winner!!")
            return "user1", player_1_total
    else:
            print("Player 2 is the winner!!!")
            return "user2", player_2_total

def take_turn():
    dice1 = generate_dice_roll() 
    dice2 = generate_dice_roll()
    return calculate_score(dice1, dice2) 

def main():
    authenticated_users = authenticate_users()
    if not authenticated_users:
        print("Authentication failed. Exiting program.")
        return
    else:
       user1, user2 = authenticated_users
       print(f"Authenticated users: {user1}, {user2}")

    player_1_total = 0
    player_2_total = 0
    
    for i in range(5):                               
        print('Round {}'.format(i + 1))
        player_1_score = take_turn()
        player_1_total += player_1_score
        print(player_1_score)
        print(player_1_total)

        player_2_score = take_turn()
        player_2_total += player_2_score
        print(player_2_score)
        print(player_2_total)

    print(player_1_total)
    print(player_2_total)

    name = ""
    highest_score = 0

    if player_1_total > player_2_total:
        name = 'user1'
        highest_score = player_1_total
        print("Player 1 is the winner!!")
    elif player_1_total < player_2_total:
        name = 'user2'
        highest_score = player_2_total
        print("Player 2 is the winner!!!")
    else:    
        name, highest_score = determine_winner(player_1_total, player_2_total)


        
    try:
        with open("high_scores.json", "r") as file:
            high_scores = json.load(file)
    except FileNotFoundError:
            # If the file does not exist, start with an empty list
            high_scores = []
    except json.JSONDecodeError:
            # If the file is empty or corrupted, start with an empty list
            high_scores = []

    new_high_score = {"name": name, "score": highest_score}
    high_scores.append(new_high_score)
    print(high_scores)

    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file, indent=4)
    if name not in high_scores or highest_score > high_scores[name]:
        high_scores[name] = highest_score
    
    
    # Check and update the highest score
    if name not in high_scores or highest_score > high_scores[name]:
        high_scores[name] = highest_score
        print(f"New high score for {name}: {highest_score}")
    else:
        print(f"No new high score. Current high score for {name}: {high_scores[name]}")

    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file, indent=4)


if __name__ == '__main__':
    main()

    