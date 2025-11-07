from typing import Annotated
from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
