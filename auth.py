def authenticate_user(username, password, user_data):
    authenticated = False

    for user in user_data:
        usr = user['username']
        passw = user['password']

        if username == usr and password == passw:
            authenticated = True
            break

    return authenticated
