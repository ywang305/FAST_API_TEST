import sys

sys.path.append("..")

from fastapi import FastAPI
from models.mock_model import Creature
from pydantic import ValidationError

app = FastAPI()


@app.get("/creatures")
def get_all() -> list[Creature]:
    from services.mock_data import get_creatures

    return get_creatures()


@app.get("/demo_bad_model/{what}")
def invalid_model(what: str) -> Creature:
    is_bad_value = what == "value"
    is_bad_type = not is_bad_value
    dragon = Creature(
        name="!" if is_bad_value else "dragon",
        description=["incorrect", "string", "list"] if is_bad_type else "*",
        country="*",
        area="*",
    )

    return dragon


@app.exception_handler(Exception)
async def model_validation_exception_handler(request, exc: Exception):
    from fastapi.responses import JSONResponse

    print(f"OMG! An model validation error!: {repr(exc)}")
    return JSONResponse(
        status_code=200,
        content={"message": exc.detail},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("mock_creatures_controller:app", reload=True)
# cd fast_api_book/intro_tutor/controllers && python mock_creatures_controller.py

# • Apply type hints to variables and functions
# • Define and use a Pydantic model
# • Return a list of models from a data source
# • Return the model list to a web client, automatically converting the model list to JSON
# . Validate Type, Validate Value
