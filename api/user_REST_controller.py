from fastapi import APIRouter

from utils.mockups import fill_users_array



app = APIRouter(prefix="/users")



USERS = fill_users_array()

@app.get("/v1/test")
async def get_user_test():

    """
    """

    return USERS