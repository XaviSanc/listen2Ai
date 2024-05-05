from fastapi import APIRouter, Path,HTTPException, status, Query

from application.user_controller import get_user_by_email_controller,add_playlist_controller
from domain.playlist import Playlist





app = APIRouter(prefix="/users")


@app.get("/v1/{email}/profile")
async def get_user_email(
     email: str = Path(..., alias=None, title=None, description='Insert user email'),
):

    """
    This endpoint returns all user information and the playlists 
    """
    try:
        return get_user_by_email_controller(email)
    except HTTPException as e:
        raise e


@app.post("/v1/{email}/playlist")
async def add_playlist(
     email: str = Path(..., alias=None, title=None, description='Insert user email'),
     playlist: str = Query(...)
):

    """
    This endpoint purpose it to add a playlist into a users playlist list
    """
    try:
        return add_playlist_controller(email, playlist)
    except HTTPException as e:
        raise e

