from fastapi import FastAPI
from app.routers.signup import signupRouter

app = FastAPI(title="Authentication Model")
app.include_router(router=signupRouter)


@app.get("/")
def home():
    return {
        "status": "server is online"
    }


