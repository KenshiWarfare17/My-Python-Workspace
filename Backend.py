from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend Python aktif 🔥"}

@app.get("/art")
def get_art():
    return {
        "title": "Beyond Imagen",
        "artist": "HOLO",
        "description": "Futuristic AI Art"
    }

@app.get("/stats")
def stats():
    return {
        "views": 1240,
        "likes": 320,
        "rating": 4.8
    }
