from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

@app.get("/hi/{who}")
def greet(who):
  return f"Hello? {who}?"


# That Body(embed=True) is needed to tell FastAPI that,
# this time, we get the value of who from the JSON-formatted request body.
# The embed part means that it should look like {"who": "Mom"} rather than just "Mom".
# http -v localhost:8000/hi who=Mom
@app.post("/hi")
def greet_from_body(who: str = Body(embed=True)):
  return f"Hello? {who}?"


# Let’s test this one just with HTTPie in Example 3-25. It uses name:value to specify an HTTP header.
# http -v PATCH localhost:8000/hi who:Dad
@app.patch("/hi")
def greet_from_header(who:str = Header()):
  return f"Hello? {who}?"

# You can inject HTTP response headers,
# http localhost:8000/header/marco/polo
@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "normal body"


#########  start server ( 2 approaches ) #############
# $ uvicorn model.src.hello:app --reload


# if __name__ == "__main__":
#   import uvicorn
#   uvicorn.run("hello:app", reload=True)
