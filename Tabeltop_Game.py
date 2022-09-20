# This file will hold the game and scenario classes

from enum import Enum
from random import randint

class Status(Enum):
  inctive = 0
  active = 1
  completed = 2
  

# TableTopGame class, this class should have start, and end methods, a list containing all currently active scenarios, a roll_dice method, 
# and a count of the total number of dice rolls
#FIXME
class TableTopGame:
  def __init__(self):
    self.is_running = False
    self.active_events = []
    self.event_descriptions_file = ""
  
  #FIXME
  def Start():
    pass
  
  def End():
    pass
  
  def RollDie(minimum, maximum):
    result = randint(minimum, maximum)
    return result
  
  def SetDescriptionLocation():
    filename = input("Enter location for event descriptions.")
  
  #TODO Finish filling out TableTopGame class

# Scenario class, this class should have a name and a description of the scenario and its best practice solution.
# It should also have a markers for inactive -> active -> deactivated
#FIXME
class Event:
  def __init__self(self, name, description, status: Enum):
    self.name = name
    self.description = description
    self.status = Status.inactive
    
  def UpdateStatus(self):
    if self.status == Status.completed:
      return
    elif self.status == Status.inactive:
      self.status = Status.active
    elif self.status == Status.active:
      self.status = Status.completed
    else:
      raise Exception(f"Event status for {self.name} not properly set.")
      
  #FIXME
  def GetDescription(filename=""):
    pass
    
