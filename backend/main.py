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
    {"id": 1, "name": "Stup Alpha", "price": 20, "category": "Stup"},
    {"id": 2, "name": "Stup Pro", "price": 30, "category": "Stup"},

    {"id": 3, "name": "Puff Fraise", "price": 10, "category": "Puff"},
    {"id": 4, "name": "Puff Mangue", "price": 12, "category": "Puff"},

    {"id": 5, "name": "Tabac Blond", "price": 8, "category": "Tabac"},
    {"id": 6, "name": "Tabac Brun", "price": 9, "category": "Tabac"},
]


@app.get("/api/ping")
def ping():
    return {"status": "connected"}

@app.get("/api/products")
def get_products():
    return products

@app.get("/api/categories")
def get_categories():
    return ["Stup","Puff","Tabac"]
    return cats
