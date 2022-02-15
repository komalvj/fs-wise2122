from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Welcome to Trip Planner!"}


@app.get("/places/{places_id}")
def read_item(places_id: int, p_name: Optional[str] = None):
    return {"places_id": places_id, "p_name": p_name}
