from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Test API")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class User(BaseModel):
    username: str
    email: str
    age: int

# База данных в памяти для тестов
fake_db = {
    "items": {
        1: {"name": "Test Item", "price": 9.99, "is_offer": True}
    },
    "users": {
        1: {"username": "testuser", "email": "test@example.com", "age": 25}
    }
}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in fake_db["items"]:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db["items"][item_id]

@app.post("/items/")
async def create_item(item: Item):
    new_id = max(fake_db["items"].keys()) + 1 if fake_db["items"] else 1
    fake_db["items"][new_id] = item.dict()
    return {"id": new_id, **item.dict()}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id not in fake_db["users"]:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db["users"][user_id]

@app.post("/users/")
async def create_user(user: User):
    if user.age < 0:
        raise HTTPException(status_code=400, detail="Age cannot be negative")
    
    new_id = max(fake_db["users"].keys()) + 1 if fake_db["users"] else 1
    fake_db["users"][new_id] = user.dict()
    return {"id": new_id, **user.dict()}
