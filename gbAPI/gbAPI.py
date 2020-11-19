"""A Module used to launch the gameboard REST API."""
from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Currently using local host / port
host = "127.0.0.1"
port = 80

@app.get("/")
def get_fastapi_docs():
    return "%s/docs" % host


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



def main():
    uvicorn.run("gbAPI.gbAPI:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    main()