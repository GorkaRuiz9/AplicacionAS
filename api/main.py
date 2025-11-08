from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import os

# --- 🔧 Configuración Mongo desde variables de entorno ---
MONGO_URI = os.environ["MONGO_URI"]
DB_NAME = os.environ["DB_NAME"]
COLLECTION_NAME = os.environ["COLLECTION_NAME"]

# --- 📦 Conexión a Mongo ---
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

app = FastAPI()

# --- 🌐 Configurar CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Ajustar según tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 🧠 Endpoint de items ---
@app.get("/items")
def get_items():
    items = list(collection.find({}, {"_id": 0}))  # quitamos _id de mongo
    return items  # devolvemos directamente la lista
