from fastapi import APIRouter



app = APIRouter(prefix="/users")




@app.get("/v1/test")
async def get_user_test():

    """
    """

    return "hello"