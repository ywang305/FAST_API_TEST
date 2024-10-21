import os
from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()



### ===   scenario 1 ====

# the dependency function:
def file_dep(owner: str): return { "file_name": os.path.basename(__file__), "owner": owner }

# http -v localhost:8000/file owner==Yao
# GET /file?owner=Yao
#
# {
#     "file_name": "controller.py",
#     "owner": "yao"
# }
@app.get("/file")
def get_file(file: dict = Depends(file_dep)) -> dict:
  return file


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("controller:app", reload=True)
