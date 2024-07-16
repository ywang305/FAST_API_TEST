from pydantic import BaseModel, Field


class Creature(BaseModel):
    name: str = Field(
        ..., min_length=2
    )  # That ... argument to Field() means that a value is required, and that there’s no default value.
    country: str
    area: str
    description: str


thing = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman",  # it's neglected
)

# print("Name is", thing.name)
# print(thing)
