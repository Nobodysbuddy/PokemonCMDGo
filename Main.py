import random

print('Crossing Tall Grass...')

wchance = [0, 0, 1]
rchance = [0, 0, 0, 0, 1]
mchance = [0, 0, 0, 0, 0, 0, 1]

pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pikachu', 'eevee']
pokemonStats = {
    'bulbasaur': {
        'name': 'Bulbasaur',
        'health': 150,
        'chance': [0, 0, 1],
        'attacks': {
            '1': 'Leaf Strike',
            '2': 'Tackle Down'
        }
    },
    'charmander': {
        'name': 'Charmander',
        'health': 150,
        'chance': [0, 0, 1],
        'attacks': {
            '1': 'Flames',
            '2': 'Hit'
        }
    },
    'squirtle': {
        'name': 'Squirtle',
        'health': 150,
        'chance': [0, 0, 1],
        'attacks': {
            '1': 'Squirt',
            '2': 'Pounce'
        }
    },
    'pikachu': {
        'name': 'Pikachu',
        'health': 125,
        'chance': [0, 0, 1],
        'attacks': {
            '1': 'Shock',
            '2': 'Pounce'
        }
    },
    'eevee': {
        'name': 'Eevee',
        'health': 125,
        'chance': [0, 0, 1],
        'attacks': {
            '1': 'Takedown',
            '2': 'Hit'
        }
    },
}
pokeballs = 5

transport = input('Walk, run or mount? : ')
if transport == 'walk':
    chance = wchance
elif transport == 'run':
    chance = rchance
elif transport == 'mount':
    chance = mchance
else:
    chance = wchance
    
def encounter():
    global pokeballs
    wildPokemon = random.choice(pokemon)
    wildPokemonStats = pokemonStats[wildPokemon]
    print('Wild', wildPokemonStats['name'], 'Encountered!')
    print('\n\n ---- Wild Pokemon Battle ---- ')
    print('\nWild', wildPokemonStats['name'] + ':')
    print('Health:', str(wildPokemonStats['health']))
    print('Attacks:', wildPokemonStats['attacks']['1'], 'and', wildPokemonStats['attacks']['2'])
    if 'yourPokemon' in globals():
        print('\nYour Pokemon:')
    else:
        print('\nReady To Catch, You Have', str(pokeballs), 'Pokeballs Remaining')
        enctmp1 = False
        while not enctmp1:
            doThrow = input('Throw Pokeball or Run? (throw/run): ')
            if doThrow == 'throw':
                if pokeballs > 0:
                    pokeballs -= 1
                    isCaught = random.choice(wildPokemonStats['chance'])
                    if isCaught == 1:
                        print(wildPokemonStats['name'], 'Was Caught!')
                        enctmp1 = True
                    else:
                        print('Oh No, The Wild', wildPokemonStats['name'], 'Broke Out!')
                else:
                    print("Oh No! You Dont Have Any Pokeballs Left!")
            elif doThrow == 'run':
                print('You Got Away Safely!')
                enctmp1 = True
    
exit = False
while not exit:
    got = random.choice(chance)
    if got == 1:
        isEncounter = True
    else:
        isEncounter = False
        
    if isEncounter:
        encounter()
    else:
        isExit = input('No Encounter, Exit? (y/n) ')
        if isExit == 'y':
            exit = True