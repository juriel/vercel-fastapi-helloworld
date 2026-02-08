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

    

    
    
    return {"message": files, "pwd": os.getcwd(), "hierarchy": generate_folder_hierarchy(".")}


# generate dictionary with folder hierachy including files and folders
# details.
# example:
# {
#     "name": "root",
#     "type": "folder",
#     "children": [
#         {
#             "name": "file1.txt",
#             "type": "file",
#             "size": 1024
#         },
#         {
#             "name": "folder1",
#             "type": "folder",
#             "children": [
#                 {
#                     "name": "file2.txt",
#                     "type": "file",
#                     "size": 2048
#                 }
#             ]
#         }
#     ]
# }

def generate_folder_hierarchy(path):
    resp = {
        "name": path,
        "type": "folder",
        "children": []
    }
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            resp["children"].append(generate_folder_hierarchy(item_path))
        else:
            resp["children"].append({
                "name": item,
                "type": "file",
                "size": os.path.getsize(item_path)
            })
    return resp


@app.get("/api/hello")
async def hello(name: str):
    return {"message": f"Hello {name}"}
# Mount the public directory at the root
#app.mount("/", StaticFiles(directory="public", html=True), name="public")

app.mount("/", StaticFiles(directory="static"), name="static")