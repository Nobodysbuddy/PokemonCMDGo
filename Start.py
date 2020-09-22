import sys
import time
import random

global starterpokemon
global name
global pokeballs

pokeballs = 5

def crosstallgrass(pbs):
    wchance = [0, 0, 1]
    rchance = [0, 0, 0, 0, 1]
    mchance = [0, 0, 0, 0, 0, 0, 1]
    
    transport = input('Walk, run or MaxSpeedTM? : ')
    if transport == 'walk':
        chance = wchance
    elif transport == 'run':
        chance = rchance
    elif transport == 'maxspeedtm':
        chance = mchance
    else:
        chance = wchance

def myhouse(sp):
    print('\n   |')
    print('  / \\')
    print(' /   \\')
    print('/     \\')
    print('|  _  |')
    print('| | | |')
    print('\nYour House: (Type The Number Of The Action You want To Do)')
    print('1] Rest ' + sp)
    print('2] Talk To Mom')
    print('3] Leave')
    
def game1(sp, pbs):
    print('\nAction Menu: (Type The Number Of The Action You want To Do)')
    print('1] Go To Your House')
    print('2] Exit Verlin City')
    print('3] Go To Prof. Oak\'s Lab')
    action1 = input('\nNo. of Action: ')
    if action1 == '1':
        crosstallgrass(pbs)
        myhouse(sp)


def chooseStarter(pokebs):
    print('\n\n1] Bulbasaur - Nature')
    print('2] Charmander - Fire')
    print('3] Squirtle - Water')
    delprint('\n\nProf. Oak: Tell me the number of the Starter you want.')
    starterpokemon = input('\nMe: ')
    if starterpokemon == '1':
        sure = input('Are You Sure That You want Bulbasaur As Your Starter? (y/n) ')
        if sure == 'y':
            delprint('\nProf. Oak: Great Then!')
            starterpokemon = 'bulbasaur'
            after1(starterpokemon, pokebs)
            return starterpokemon
        else:
            chooseStarter()
    elif starterpokemon == '2':
        sure = input('Are You Sure That You want Charmander As Your Starter? (y/n) ')
        if sure == 'y':
            delprint('\nProf. Oak: Great Then!')
            starterpokemon = 'charmander'
            after1(starterpokemon, pokebs)
            return starterpokemon
        else:
            chooseStarter()
    elif starterpokemon == '3':
        sure = input('Are You Sure That You want Squirtle As Your Starter? (y/n) ')
        if sure == 'y':
            delprint('\nProf. Oak: Great Then!')
            starterpokemon = 'squirtle'
            after1(starterpokemon, pokebs)
            return starterpokemon
        else:
            chooseStarter()
    else:
        print('Invalid Number')
        chooseStarter()
        
        
def after1(starter, catchballs):
    def explain1():
        delprint('\nProf. Oak: Now before you move on I will explain you some basic things.')
        delprint('\nProf. Oak: Your '+ starter + ' will \'evolve\' after 20 battles and after that it will evolve after 40 battles.')
        delprint('\nProf. Oak: On your journey you will find trainers who would like to battle with you. If you win they would pay you Pokecoins and if you win you will have to pay them.')
        delprint('\nProf. Oak: And if you go to anywhere you will have to cross tall grass which would be blooming with wild pokemon.')
        delprint('\nProf. Oak: These pokemon could be caught and befriended with pokeballs or be battled with.')
        delprint('\nProf. Oak: So, you are all set to go on your Pokemon Adventure!')
        game1(starter, catchballs)
    delprint('\nProf. Oak: So, You Starter is ' + starter + '!')
    skip1 = input('\nSkip? (y/n) ')
    if skip1 == 'y':
        game1(starter, catchballs)
    else:
        explain1()
    
def startingDialogs(pballs):
    delprint('\nProf. Oak: Hello -')
    delprint('\nProf. Oak: Ahh.. Im such a dumb man... So, What is your name little fella?')
    name = input('\nMe: ')
    delprint('\nProf. Oak: Oh ya it was ' + name + ', I hope I wont forget again...')
    delprint('\nProf. Oak: So, Hello ' + name + '! This is me, Professer Oak!')
    delprint('\nProf. Oak: I study Pokemon, the sweet creatures present all around the world.')
    delprint('\nProf. Oak: And I want you to help me research... So, prepare as you enter your own Pokemon Adventure!')
    delprint('\nProf. Oak: But before I let you go, You will need to get a Starter Pokemon!')
    delprint('\nProf. Oak: A Starter Pokemon is a Pokemon that stays with you throughout your Adventure.')
    delprint('\nProf. Oak: So tell me, Which Starter Pokemon do you want?')
    pokestarter = chooseStarter(pballs)

print(' ----- Pokemon CMDGo ----- ')

def delprint(pr):
    for c in pr:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
        
skip = input('Skip? (y/n) ')
if skip == 'y':
    chooseStarter()
else:
    startingDialogs(pokeballs)
