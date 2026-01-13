from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import hmac
from urllib.parse import parse_qs

import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://telegram-shop-93m.pages.dev", "https://t.me"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================
# 🔐 TELEGRAM AUTH
# ============================
def verify_telegram(init_data: str):
    parsed = parse_qs(init_data)

    if "hash" not in parsed:
        return False

    received_hash = parsed.pop("hash")[0]

    data_check_string = "\n".join(
        f"{k}={v[0]}" for k, v in sorted(parsed.items())
    )

    secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
    calculated_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256
    ).hexdigest()

    return calculated_hash == received_hash


@app.middleware("http")
async def telegram_auth(request: Request, call_next):
    # On protège seulement les endpoints produits
    if request.url.path.startswith("/api"):
        # iOS Safari ne passe pas toujours les headers
        init_data = request.headers.get("x-telegram-init-data")

        # Si l'appel vient de Telegram WebApp, on autorise
        if request.headers.get("origin", "").startswith("https://telegram-shop-93m.pages.dev"):
            return await call_next(request)

        # Sinon on vérifie la signature Telegram
        if init_data and verify_telegram(init_data):
            return await call_next(request)

        # Sinon on bloque
        raise HTTPException(status_code=403, detail="Unauthorized Telegram")

    return await call_next(request)
    
# ============================
# PRODUCTS (TES DONNÉES EXACTES)
# ============================

products = [
    # --------------------
    # PUFF (5 photos)
    # --------------------
    {
        "id": 1,
        "name": "Puff Fraise",
        "price": 10,
        "category": "Puff",
        "image": "https://telegram-shop-93m.pages.dev/img/puff1.jpg",
        "description": "Saveur fraise douce. 600 bouffées, tirage fluide."
    },
    {
        "id": 2,
        "name": "Puff Mangue",
        "price": 11,
        "category": "Puff",
        "image": "https://telegram-shop-93m.pages.dev/img/puff2.jpg",
        "description": "Mangue tropicale. Goût intense et sucré."
    },
    {
        "id": 3,
        "name": "Puff Myrtille",
        "price": 12,
        "category": "Puff",
        "image": "https://telegram-shop-93m.pages.dev/img/puff3.jpg",
        "description": "Myrtille fraîche. Sensation légère."
    },
    {
        "id": 4,
        "name": "Puff Ice",
        "price": 13,
        "category": "Puff",
        "image": "https://telegram-shop-93m.pages.dev/img/puff4.jpg",
        "description": "Menthol glacé. Hit fort."
    },
    {
        "id": 5,
        "name": "Puff Mix Fruits",
        "price": 14,
        "category": "Puff",
        "image": "https://telegram-shop-93m.pages.dev/img/puff5.jpg",
        "description": "Cocktail de fruits premium."
    },
]

# --------------------
# STUP (vidéos)
# 8,11,15,16 supprimés
# --------------------
stup_descriptions = {
    1: """🟣 FRESH FROZEN WHOLE PLANT 🟣

✅ VARIÉTÉS
• PURPLE MOLT’S 🧬

🧬 Les amis, ce WHOLE PLANT FRESH FROZEN est tout simplement une dinguerie.
Sa méthode de traitement spécifique consiste à récolter la plante entière (fleurs, feuilles, tiges),
non séchée, puis directement mise en congélation après la récolte.
Cela donne un produit à très haute teneur en THC et d’une pureté légendaire.

QUANTITÉS DISPO :
1G 🟣 2G 🟣 5G 🟣 10G 🟣 25G 🟣 50G 🟣 100G 🟣 200G 🟣 500G 🟣 1K 🟣 +PV

⭕️ PRIX EN PV ⭕️
""",
    2: """🇺🇸 🍯 LIVE ROSIN PUR 🍯 🇺🇸

✅ VARIÉTÉS
• LEMON 🍋

🔥 Et de 3 ! Une troisième pépite que nous vous avons ramenée.
Le LIVE ROSIN PUR est un concentré de cannabis haut de gamme (Fresh Frozen ou WPFF),
transformé d’abord en LIVE HASH (Bubble Hash), puis pressé à chaud (Rosin),
sans aucun solvant chimique (ni butane, ni CO2, ni propane).

Souvent apprécié pour sa pureté, son goût prononcé et sa méthode d’extraction sans solvant.

💡 Pur signifie sans additif, sans terpènes ajoutés, sans coupe, uniquement la résine de la plante.

QUANTITÉS DISPO :
1G 🍯 3G 🍯 5G 🍯 10G 🍯 25G 🍯 50G 🍯 100G 🍯

⭕️ PRIX EN PV ⭕️
""",
    3: "Stup 3 – Plus puissant, montée rapide.",
    4: "Stup 4 – Effet long et profond.",
    5: """🇺🇸 CALI US PREMIUM SHELF 🇺🇸

✅ VARIÉTÉS
• GELATO 33 🍦

🔥 Une cali unique et spectaculaire.
La GELATO 33 est un mélange de bonbon et de notes boisées.
Un vrai régal pour les papilles.

DISPO :
10G 🇺🇸 25G 🇺🇸 50G 🇺🇸 100G 🇺🇸 200G 🇺🇸 500G 🇺🇸 1K + PV

⭕️ PRIX EN PV ⭕️
""",
    6: "Stup 6 – Mélange spécial.",
    7: "Stup 7 – Version intense.",
    9: "Stup 9 – Ultra premium.",
    10: """🇺🇸 🍯 PIATELLA UNCLE’S FARM 🍯 🇺🇸

🇺🇸 De la folie à tous les niveaux.
Ce PIATELLA importé tout droit des USA vous fera voyager.

QUANTITÉS DISPO :
1G 🍯 3G 🍯 5G 🍯 10G 🍯 25G 🍯 50G 🍯 100G 🍯

⭕️ PRIX EN PV ⭕️
""",
    12: "Stup 12 – Très fort.",
    13: "Stup 13 – Effet stable.",
    14: """🍫 STATICSIFT 🍫

✅ VARIÉTÉS
• PINEAPPLE 🍍

🔥 Un STATICSIFT de folie.
Terps bien développés, encore glassy, du très lourd.

QUANTITÉS DISPO :
10G 🍍 25G 🍍 50G 🍍 100G 🍍 200G 🍍 500G 🍍 1K 🍍 +PV

⭕️ PRIX EN PV ⭕️
""",
    17: "Stup 17 – Version ultime."
}

for i, desc in stup_descriptions.items():
    products.append({
        "id": 100 + i,
        "name": f"Stup {i}",
        "price": 20 + i,
        "category": "Stup",
        "video": f"https://telegram-shop-93m.pages.dev/videos/stup{i}.mp4",
        "description": desc
    })

# --------------------
# TABAC
# --------------------
products.append({
    "id": 300,
    "name": "Tabac Blond",
    "price": 8,
    "category": "Tabac",
    "video": "https://telegram-shop-93m.pages.dev/videos/tabac1.mp4",
    "description": "Tabac blond classique, goût doux."
})

# ============================
# API
# ============================
@app.get("/api/ping")
def ping():
    return {"status": "connected"}

@app.get("/api/products")
def get_products():
    return products

@app.get("/api/categories")
def get_categories():
    return ["Stup", "Puff", "Tabac"]
