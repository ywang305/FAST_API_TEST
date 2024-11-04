from fastapi import APIRouter

router = APIRouter(prefix = "/explorer")

@router.get("/")
def top() -> list:
  import sys
  return sys.path

### http -b  -> only print resp body
# (.venv) ydwang@ICN-NQPP9CXNMW chap8_subrouters % http -b localhost:8000/explorer/

