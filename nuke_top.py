from random import randint
from os import system
import sys

if __name__ == '__main__':
  system('clear')
  print('Welcome to NUKE TOP')
  _ = input(f'\nPress [ENTER] to continue . . . ')
  chances = 25
  system('clear')
  print('WARNING\nNuclear raid sirens are going off. Its the absolute worst case scenario.')
  _ = input(f'\nPress [ENTER] to roll to see if you are outside groud zero . . . ')
  result = randint(0, 100)
  system('clear')
  if result > chances:
    chances += 25
    print('You were outside of ground zero!')
    _ = input('Press [ENTER] to see if you survive the resulting shockwaves . . . ')
    result = randint(0, 100)
    system('clear')
    if result > chances:
      chances += 25
      print("Congratulations, you survived the shockwave.")
      _  = input('Press [ENTER] to see if you survive radiation poisoning . . . ')
      result = randint(0, 100)
      system('clear')
      if result > chances:
        chances += 25
        print("Wow! You're a hardened survivor!")
        _ = input('Press [ENTER] to see if you survive starvation during the nuclear winter . . . ')
        result = randint(0, 100)
        system('clear')
        if result > chances:
          print(f'You survived! I suspect you of cheating but I\'ll give you the benefit of the doubt. :)')
        else:
          print(f'Your life depreciated to the point of negligible valuation. You made it pretty far though. B(')
      else:
        print(f'You withered away from radiation poisoning. XP\nBye')
    else:
      print(f'You were flattened by the shockwaves. >:(\nBye')
  else:
    print(f'You were disentigrated by the initial explosion. :(\nBye')

    