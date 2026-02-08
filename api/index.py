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
    return {"message": os.getcwd()}

@app.get("/api/hello")
async def hello(name: str):
    return {"message": f"Hello {name}"}
# Mount the public directory at the root
#app.mount("/", StaticFiles(directory="public", html=True), name="public")

#app.mount("/", StaticFiles(directory="public"), name="public")