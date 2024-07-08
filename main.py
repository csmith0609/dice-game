import json
from dice import generate_dice_roll
from auth import authenticate_user

with open('users.json') as f:
    d = json.load(f)
    print(d)

user_input = input("what is your username?")
password_input = input("what is your password?")


val = authenticate_user(user_input, password_input, d)
print(val)

print(generate_dice_roll())
print(generate_dice_roll())
