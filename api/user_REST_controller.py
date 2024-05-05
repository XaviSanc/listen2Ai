from fastapi import APIRouter, Path

from application.user_controller import get_user_by_email_controller





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
    except Exception as e:
        return e


