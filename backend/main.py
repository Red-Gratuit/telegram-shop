from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {"id": 1, "name": "Pack Starter", "price": 15, "category": "Packs"},
    {"id": 2, "name": "Résine Premium", "price": 25, "category": "Résine"},
    {"id": 3, "name": "Recharge 10ml", "price": 10, "category": "Recharges"},
    {"id": 4, "name": "Recharge 30ml", "price": 20, "category": "Recharges"},
    {"id": 5, "name": "Accessoire Pro", "price": 12, "category": "Accessoires"},
]

@app.get("/api/ping")
def ping():
    return {"status": "connected"}

@app.get("/api/products")
def get_products():
    return products

@app.get("/api/categories")
def get_categories():
    cats = sorted(set(p["category"] for p in products))
    return cats
