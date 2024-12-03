import requests
import os

from dotenv import load_dotenv
from models.pokemon import Pokemon
from typing import Union

load_dotenv()

def get_pokemon(pokemon: str) -> Union[Pokemon, str]:
    """ Función que obtiene un pokemon a partir de la api asd a partir del nombre obtenido.
        De no encontrar el pokemon deberia devolver un error denotando la inexistencia.
    """
    try:

        poke_obj = requests.get(os.getenv('POKEAPI_URL')+pokemon)

    except requests.exceptions.RequestException:
        print(f"Error al conectar al servidor")
        return None

    if poke_obj.status_code == 200:

        response = poke_obj.json()
        hp = None
        attack = None
        defense = None
        special_attack = None
        special_defense = None
        speed = None

        for idx in response['stats']:
            hp = idx['base_stat'] if idx['stat']['name'] == 'hp' else hp
            attack = idx['base_stat'] if idx['stat']['name'] == 'attack' else attack
            defense = idx['base_stat'] if idx['stat']['name'] == 'defense' else defense
            special_attack = idx['base_stat'] if idx['stat']['name'] == 'special-attack' else special_attack
            special_defense = idx['base_stat'] if idx['stat']['name'] == 'special-defense' else special_defense
            speed = idx['base_stat'] if idx['stat']['name'] == 'speed' else speed

        new_pokemon = Pokemon(
                            name = response['name'].upper(),
                            hp = hp,
                            attack = attack,
                            defense = defense,
                            special_attack = special_attack,
                            special_defense = special_defense,
                            speed = speed
                            )
    else:
        return None

    return new_pokemon