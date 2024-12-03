import random

from models.pokemon import Pokemon
from typing import Union


class BattleCalculation():

    def get_fastests_pokemon(self, first: Pokemon, second: Pokemon) -> list:
        """ Indentifica al pokemon más veloz y en caso de empate elige al primero cargado.
        """
        
        if first.speed > second.speed:
            return [first, second]
        elif second.speed > first.speed:
            return [second, first]
        else:
            return [first, second]
    
    def get_ramdom_attack(self, max_value: int, battle_round: list, order: int) -> Union[None, str]:
        """ Setea el atacante y el defensor por cada turno.
            Determina el valor de damage para el ataque y lo aplica.}

            1)  damage = (attack / defense del oponente) * 10
            2)  damage = (special-attack / special-defense del oponente) * 10
        """

        attack_turn = 0 if order % 2 == 0 else 1
        attacker = battle_round[attack_turn]
        defender = battle_round[0] if attack_turn == 1 else battle_round[1]
        number = random.randint(1, max_value)

        if number % 2 == 0:
            damage = round((attacker.attack / defender.defense)*10, 2)
        else:
            damage = round((attacker.special_attack / defender.special_defense)*10, 2)

        print("")
        print(f'\033[32mTurno {order+1}: {attacker.name} ataca a {defender.name} y causa {damage} puntos de daño.\033[0m')
        print("     Nuevo estado de ambos pokemones:")
        print("")
        print(attacker)
        print("-------------------------------------")
        # defender.hp -= damage
        defender.hp = round(defender.hp - damage, 2)
        print(defender)
        print("")

        return f'\033[31mEl pokemon {defender.name} ya no puede continuar, el Ganador es el pokemon {attacker.name}\033[0m' if defender.hp <= 0 else None
    

    def winner_calculation(self, battle_status: list) -> list:
        """ Función que determina el ganador, perdedor y/o empate
        """

        if battle_status[0].hp > battle_status[1].hp:
            return f'\033[31mSin embargo el GANADOR es {battle_status[0].name} y el PERDEDOR es {battle_status[1].name}\033[0m'
        elif battle_status[0].hp < battle_status[1].hp:
            return f'\033[31mSin embargo el GANADOR es {battle_status[1].name} y el PERDEDOR es {battle_status[0].name}\033[0m'
        else:
            return f'\033[31mHemos obtenido un EMPATE entre {battle_status[0].name} y {battle_status[1].name}\033[0m'