import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    app_model_name = os.path.basename(__file__)[:-3]
    uvicorn.run(f"{app_model_name}:app", host="127.0.0.1", port=8889, reload=True)
