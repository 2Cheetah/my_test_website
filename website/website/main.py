'''FastAPI app and its handlers'''
from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    '''root handler'''
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    '''/items handler'''
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
