from utils.mockups import fill_users_array

USERS = fill_users_array()

def get_user_by_email_persistance(email):

    for user in USERS:
        if user.email == email:
            return user
    
    raise Exception

def add_playlist_persistence(email,playlist_schema):
    
    for user in USERS:
        if user.email == email:
            user.playlist.append(playlist_schema)
