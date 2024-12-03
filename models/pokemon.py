from pydantic import BaseModel

class Pokemon(BaseModel):
    name : str
    hp : float
    attack : int
    defense : int
    special_attack : int
    special_defense: int
    speed : int
