from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
secret_user: str = "newphone"
secret_password: str = "whodis?"

basic: HTTPBasicCredentials = HTTPBasic()

# http -q -a newphone:whodis? localhost:8000/who
@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
  if (creds.username == secret_user and creds.password == secret_password):
    return {"username": creds.username, "password": creds.password}
  raise HTTPException(status_code=401, detail="Hey!")

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("auth:app", reload=True)
