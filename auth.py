import json

def authenticate_user(username, password, user_data):
    for user in user_data:
        usr = user['username']
        passw = user['password']

        if username == usr and password == passw:
            return True
    return False

def authenticate_users():
    with open('users.json') as f:
        users = json.load(f)
        print(users)

    user_input = input("Player 1, what is your username?")
    password_input = input("Player 1, what is your password?")

    user2_input = input("Player 2, what is your username?")
    password2_input = input("Player 2, what is your password?")

    if not authenticate_user(user_input, password_input, users): 
        return False
    if not authenticate_user(user2_input, password2_input, users): 
        return False

    return user_input, user2_input