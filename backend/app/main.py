from fastapi import FastAPI

app = FastAPI(title="Authentication Model")


@app.get("/")
def home():
    return {
        "status": "server is online"
    }


