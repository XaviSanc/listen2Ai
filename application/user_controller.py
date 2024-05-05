from loguru import logger
from domain.user import User
from persistence.user_persistance import get_user_by_email_persistance, add_playlist_persistence
from domain.playlist import Playlist
from fastapi import HTTPException, status


def get_user_by_email_controller(email):

    try:
        user = get_user_by_email_persistance(email)
    except Exception as e:
        logger.error(e)
        raise  HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist",
        )
    return User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        playlist=filter_user_playlist(user)
    )


def filter_user_playlist(user: User) -> User:
    filtered_playlists = []
    for playlist in user.playlist:
        filtered_playlists.append({
            "name": playlist.name,
            "likes": playlist.likes
        })
    return filtered_playlists


def add_playlist_controller(email, playlist):
    try:
        user = get_user_by_email_controller(email)
    except HTTPException as e:
        raise e
    if user:
        if is_playlist_duplicated(user,playlist):
            raise  HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Playlist {playlist} already exists",
        )
        try:
            playlist_schema = Playlist(name=playlist)
            add_playlist_persistence(email, playlist_schema)
        except Exception as e:
            logger.error(e)
            raise  HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"An error occured while creating the {playlist} playlist",
        )
        return f"Playlist {playlist} has been created"


def is_playlist_duplicated(user: User, playlist_name: str) -> bool:
    for playlist in user.playlist:
        if playlist_name in playlist.name:
            return True
    return False
