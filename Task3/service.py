from fastapi import FastAPI
from starlette.responses import JSONResponse
import random

app = FastAPI()

@app.post("/inverse")
async def inverse(data: dict) -> JSONResponse:
    inverse_data = {v: k for k, v in data.items()}
    return JSONResponse(content=inverse_data, status_code=200)

@app.get("/unstable")
async def unstable() -> JSONResponse:

    responses = [JSONResponse(content="HAPPY", status_code=200),
                JSONResponse(content="UNHAPPY", status_code=400)]

    response = random.choice(responses)

    return response