import os
import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}

from hypercorn.config import Config
from hypercorn.asyncio import serve

config = Config()
port = int(os.getenv("PORT", "8000"))
config.bind = [f"0.0.0.0:{port}"]
asyncio.run(serve(app, config))

# pipreqs . --encoding=utf8 --force
