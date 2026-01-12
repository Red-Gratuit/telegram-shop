from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser ton site Cloudflare
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://telegram-shop-93m.pages.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ping")
def ping():
    return {"status": "connected"}

@app.get("/api/products")
def products():
    return [
        {"id": 1, "name": "Kebab XL", "price": 7.5},
        {"id": 2, "name": "Frites", "price": 3.0},
        {"id": 3, "name": "Boisson", "price": 2.0}
    ]
