from fastapi import FastAPI

app = FastAPI()

# Route GET simple
@app.get("/")
def home():
    return {"message": "Bonjour depuis FastAPI !"}

# Route avec paramètre
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "nom": "Alice"}

# Route POST avec body
from pydantic import BaseModel

class User(BaseModel):
    nom: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {"message": f"Utilisateur {user.nom} créé", "age": user.age}