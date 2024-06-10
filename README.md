# FAST_API_TEST
## fastapi


ref <<OReilly.FastAPI.2023.11.pdf>>

pip install fastapi uvicorn

#########  start server ( 2 approaches ) #############
- explicitly:  `$ uvicorn model.src.hello:app --reload`

- internal:
```py
if __name__ == "__main__":
  import uvicorn
  uvicorn.run("hello:app", reload=True)
```



## Deploy
[Baseten](https://docs.baseten.co/deploy/overview), with [Truss](https://truss.baseten.co/quickstart)

there is a test.py that deployed to baseten for testing

note> api key is stored in `~/.trussrc `
