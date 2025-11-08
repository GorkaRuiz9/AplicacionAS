from fastapi import APIRouter, Request, HTTPException
from pymongo import MongoClient
import os

router = APIRouter()

MONGO_URI = os.environ["MONGO_URI"]
DB_NAME = os.environ["DB_NAME"]

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
favoritos_collection = db["favoritos"]  # Mongo crea la colección automáticamente si no existe

@router.get("")
def get_favoritos():
    favoritos = list(favoritos_collection.find({}, {"_id": 0}))
    return favoritos

@router.post("")
async def add_favorite(request: Request):
    data = await request.json()  # obtenemos el JSON tal cual viene

    # Comprobar si ya existe un favorito con el mismo ItemID
    item_id = data.get("r-itemid")
    if item_id is None:
        raise HTTPException(status_code=400, detail="Falta el campo ItemID")

    exists = favoritos_collection.find_one({"r-itemid": item_id})
    if exists:
        raise HTTPException(status_code=400, detail=f"El item con ItemID {item_id} ya está en favoritos")

    favoritos_collection.insert_one(data)
    return {"message": "Favorito añadido correctamente"}
