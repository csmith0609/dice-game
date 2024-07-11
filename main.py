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
            user1 = "Player 1"
            print("Player 1 is the winner!!")
            return user1, player_1_total
    else:
            user2 = "Player 2"
            print("Player 2 is the winner!!!")
            return user2, player_2_total

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
        name = user1
        highest_score = player_1_total
        print("Player 1 is the winner!!")
    elif player_1_total < player_2_total:
        name = user2
        highest_score = player_2_total
        print("Player 2 is the winner!!!")
    else:    
        name, highest_score = determine_winner(player_1_total, player_2_total)

    try:
        with open("high_scores.json", "r") as file:
            high_scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        high_scores = []

    new_high_score = {"name": name, "score": highest_score}
    high_scores.append(new_high_score)

    # Sort the high scores in descending order based on score
    sorted_high_scores = sorted(high_scores, key=lambda x: x["score"], reverse=True)

    # Display only the top 5 high scores
    print("Top 5 High Scores:")
    for idx, score in enumerate(sorted_high_scores[:5], start=1):
        print(f"{idx}. {score['name']} - {score['score']}")

    # Save all high scores back to the file
    with open("high_scores.json", "w") as file:
        json.dump(sorted_high_scores, file, indent=4)

if __name__ == '__main__':
    main()