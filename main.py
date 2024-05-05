from starlette.responses import RedirectResponse
from fastapi import FastAPI
from api import user_REST_controller
import uvicorn

app = FastAPI(title='Listen2AI')

API_PREFIX = "/api"

app.include_router(user_REST_controller.app, prefix=f"{API_PREFIX}", tags=["Users"])



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


@app.get("/")
async def root():
    #return {"This is myDAmicroservices. Please go to /docs to open the details"}
    return RedirectResponse(url="/docs")

"""
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""