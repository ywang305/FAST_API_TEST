from fastapi import FastAPI

app = FastAPI()



# echo request body in respose with JSON
#
# -- start
# > python fast_api_book/chap3_response_model/echo_controller.py
#
# -- request
# > echo -n '{"hello": "world", "referrals": ["abc", "def"], "address":{"ountry":"USA", "post":"NY11300"} }' | http -v localhost:8000/echo q==1000
#
# -- response
# {
#     "body": {
#         "address": {
#             "ountry": "USA",
#             "post": "NY11300"
#         },
#         "hello": "world",
#         "referrals": [
#             "abc",
#             "def"
#         ]
#     },
#     "q": "1000"
# }
@app.post("/echo")
def echo(body: dict, q: str|None) -> dict: # q is optional query paramter
  return { "body": body, "q": q }


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("echo_controller:app", reload=True, port=8000)
