from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)


@app.get("/pwd")
async def pwd():
    # list all files in the current directory
    files = os.listdir(".")
    return {"message": files, "pwd": os.getcwd()}

@app.get("/api/hello")
async def hello(name: str):
    return {"message": f"Hello {name}"}
# Mount the public directory at the root
#app.mount("/", StaticFiles(directory="public", html=True), name="public")

app.mount("/", StaticFiles(directory="static"), name="static")