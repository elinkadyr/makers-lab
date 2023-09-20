from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Модель данных для товара
class Item(BaseModel):
    id: int
    name: str
    price: float

# База данных
db = []

@app.get("/")
async def root():
    return "FASTAPI Online Shop"

# Создание товара
@app.post("/items")
async def create_item(item: Item):
    db.append(item)
    return {"message": "Item created successfully"}

# Получение всех товаров
@app.get("/items")
async def get_all_items():
    return db

# Получение конкретного товара по id
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    return {"message": "Item not found"}

# Обновление товара
@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(db):
        if item.id == item_id:
            db[i] = updated_item
            return {"message": "Item updated successfully"}
    return {"message": "Item not found"}

# Удаление товара
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(db):
        if item.id == item_id:
            del db[i]
            return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}
