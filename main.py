from typing import Annotated
from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel
from dotenv import load_dotenv
from apis.login import router as login_router

load_dotenv()


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(login_router)