from fastapi import FastAPI
from web import explorer

app = FastAPI()


app.include_router(explorer.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
