from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import items, favoritos

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 🔗 Incluir router ---
app.include_router(items.router, prefix="/items")
app.include_router(favoritos.router, prefix="/favoritos")
