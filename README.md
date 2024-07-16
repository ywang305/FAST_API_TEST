# FAST_API_TEST
## fastapi


ref <<OReilly.FastAPI.2023.11.pdf>>

pip install fastapi uvicorn

1. [fast api tour](./model/src/hello.py) \
#########  start server ( 2 approaches ) #############
- explicitly:  `$ uvicorn model.src.hello:app --reload`

- internal:
```py
if __name__ == "__main__":
  import uvicorn
  uvicorn.run("hello:app", reload=True)
```

2. [async starlette](./model/src/greet_async.py) \
uvicorn model.src.greet_async:app




## Deploy
[Baseten](https://docs.baseten.co/deploy/overview), with [Truss](https://truss.baseten.co/quickstart)

there is a test.py that deployed to baseten for testing

note> api key is stored in `~/.trussrc `
