USERS = {
    "alice": "pass123",
    "bob": "secret",
    "steve": "nicks"
}

def authenticate(username, password):
    return USERS.get(username) == password
