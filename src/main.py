from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "message": "hello, deployed",
        "server_time_utc": datetime.now(timezone.utc).isoformat(),
    }