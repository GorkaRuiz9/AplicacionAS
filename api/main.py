from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import items, favoritos, predictor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(items.router, prefix="/items")
app.include_router(favoritos.router, prefix="/favoritos")
app.include_router(predictor.router, prefix="/predictor")