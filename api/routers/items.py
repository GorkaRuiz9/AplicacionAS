from fastapi import APIRouter
from pymongo import MongoClient
import os

router = APIRouter()

MONGO_URI = os.environ["MONGO_URI"]
DB_NAME = os.environ["DB_NAME"]
COLLECTION_NAME = "items"


client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


@router.get("")
def get_items():
    items = list(collection.find({}, {"_id": 0}))  # quitamos _id de mongo
    return items
