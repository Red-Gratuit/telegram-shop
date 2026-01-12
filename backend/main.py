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
    # PUFF (5 photos)
    {"id": 1, "name": "Puff 1", "price": 10, "category": "Puff",
     "image": "https://telegram-shop-93m.pages.dev/img/puff1.jpg"},
    {"id": 2, "name": "Puff 2", "price": 11, "category": "Puff",
     "image": "https://telegram-shop-93m.pages.dev/img/puff2.jpg"},
    {"id": 3, "name": "Puff 3", "price": 12, "category": "Puff",
     "image": "https://telegram-shop-93m.pages.dev/img/puff3.jpg"},
    {"id": 4, "name": "Puff 4", "price": 13, "category": "Puff",
     "image": "https://telegram-shop-93m.pages.dev/img/puff4.jpg"},
    {"id": 5, "name": "Puff 5", "price": 14, "category": "Puff",
     "image": "https://telegram-shop-93m.pages.dev/img/puff5.jpg"},

    # STUP (17 vidéos – branding/fictif)
    *[
        {"id": 100+i, "name": f"Stup {i+1}", "price": 20+i, "category": "Stup",
         "video": f"https://telegram-shop-93m.pages.dev/videos/stup{i+1}.mp4"}
        for i in range(17)
    ],

    # TABAC (1 vidéo)
    {"id": 300, "name": "Tabac", "price": 8, "category": "Tabac",
     "video": "https://telegram-shop-93m.pages.dev/videos/tabac1.mp4"},
]

@app.get("/api/ping")
def ping():
    return {"status": "connected"}

@app.get("/api/products")
def get_products():
    return products

@app.get("/api/categories")
def get_categories():
    return ["Stup", "Puff", "Tabac"]
    return cats
