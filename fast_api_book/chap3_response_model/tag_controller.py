from fastapi import FastAPI
from datetime import datetime
from model.tag import TagIn, Tag, TagOut

app = FastAPI()


#
# Test with httpie:
#
# http -v localhost:8000/mom tag=me
#
# {
#     "created": "2024-10-11T14:02:33.451036",
#     "tag": "me"
# }
#
@app.post('/')
def create(tag_in: TagIn) -> TagOut:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.now(), secret="shhhh")
    print(f'created tag = #{tag}')
    return tag


#
# Test with httpie:
#
# http -v localhost:8000/mom
#
# {
#     "created": "2024-10-11T13:58:34.696304",
#     "tag": "mom"
# }
#
@app.get('/{tag_str}')
def get_one(tag_str: str) -> TagOut:
    tag: Tag = Tag(tag=tag_str, created=datetime.now(), secret="shhhh")
    print(f'retreial tag = #{tag}')
    return tag

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("tag_controller:app", reload=True)
