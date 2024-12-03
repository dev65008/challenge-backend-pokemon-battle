import sys
import os

from get_pokemon.poket_api import get_pokemon
from calculations.battle_calculation import BattleCalculation
from dotenv import load_dotenv

load_dotenv()

def instructions() -> None:
    """Instrucciones que se vayan conciderando necesarias para el uso de la app de batallas pokemon.
    """
    print('')
    print(f'\033[32m            Batalla Pokemon.\033[0m')

def terminal_in() -> None:
    """ Control de ingreso de nombres de los pokemones a entrar en batalla.
        Se verifica que sean 2(dos).
    """
    if (len(sys.argv) == 3):

        print('')
        print('-------------------------------------------------------------------')
        first_pokemon = get_pokemon(sys.argv[1])
        print(first_pokemon) if first_pokemon != None else print('No encontrado')
        print('-------------------------------------------------------------------')
        second_pokemon = get_pokemon(sys.argv[2])
        print(second_pokemon) if second_pokemon != None else print('No encontrado')
        print('-------------------------------------------------------------------')
        print('')

        if (first_pokemon is None or second_pokemon is None):
            print('')
            print(f'Alguno de los valores no fue encontrado')
            print(first_pokemon) if first_pokemon != None else print(f'No se encontró al pokemon {sys.argv[1]}')
            print(second_pokemon) if second_pokemon != None else print(f'No se encontró al pokemon: {sys.argv[2]}')

        else:
            print(f'\033[32m            ARRANCA LA BATALLA.\033[0m')
            print('')

            battle = BattleCalculation()
            # [fastest, slowest] 
            battle_status = battle.get_fastests_pokemon(first_pokemon, second_pokemon)

            for idx in range(int(os.getenv('BATTLE_QTY'))):
                scoring = battle.get_ramdom_attack(int(os.getenv('RAMDOM_MAX')), battle_status, idx)
                if scoring != None:
                    print(scoring)
                    break
            
            if scoring == None:
                result = battle.winner_calculation(battle_status)
                print(f'\033[31mTerminadas las batallas ambos pokemones aun disponen de fuerza....\033[0m')
                print(result)


    else:
        print(f'La cantidad de pokemones ingresados es de {len(sys.argv)-1} y debe ser de 2(dos) nombres por batalla.')

if __name__ == '__main__':
    instructions()
    terminal_in()