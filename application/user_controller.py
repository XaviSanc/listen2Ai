

from domain.user import User
from persistence.user_persistance import get_user_by_email_persistance
from fastapi import HTTPException, status

def get_user_by_email_controller(email):

    try:
        user = get_user_by_email_persistance(email)
    except Exception as e:
        raise  HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist",
        )
    return User(
        username = user.username,
        email = user.email,
        full_name = user.full_name,
        playlist = filter_user_playlist(user)
    )

def filter_user_playlist(user: User) -> User:
    filtered_playlists = []
    for playlist in user.playlist:
        filtered_playlists.append({
            "name": playlist.name,
            "likes": playlist.likes
        })
    return filtered_playlists