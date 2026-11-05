from fastapi import FastAPI
from app.routers.signup import signupRouter
from app.routers.login import LoginRouter

app = FastAPI(title="Authentication Model")
app.include_router(router=signupRouter)
app.include_router(router=LoginRouter)


@app.get("/")
def home():
    return {
        "status": "server is online"
    }


