# This file will hold the game and scenario classes

from enum import Enum
from random import randint

# TableTopGame class, this class should have start, restart, and end methods, a list containing all currently active scenarios, a roll_dice method, 
# and a count of the total number of dice rolls
#FIXME
class TableTopGame:
  def __init__(self):
    pass
  
  #FIXME
  def Start():
    pass
  
  def RollDie(minimum, maximum):
    result = randint(minimun, maximum)
    return result
  
  

# Scenario class, this class should have a name and a description of the scenario and its best practice solution.
# It should also have a markers for inactive -> active -> deactivated
#FIXME
class Scenario:
  pass
