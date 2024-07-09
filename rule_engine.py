from dice import generate_dice_roll

def calculate_score(dice1, dice2):
    total_score = dice1 + dice2

    total_score += 10 if total_score % 2 == 0 else -5
    if dice1 == dice2: total_score += generate_dice_roll()
    if total_score < 0: total_score = 0
    return total_score
