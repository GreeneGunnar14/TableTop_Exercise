# This file will hold the game and scenario classes

from enum import Enum
from hashlib import new
from random import randint

class Status(Enum):
  inctive = 0
  active = 1
  completed = 2
  

# TableTopGame class, this class should have start, and end methods, a list containing all currently active scenarios, a roll_dice method, 
# and a count of the total number of dice rolls
#FIXME
class TableTopGame:
  def __init__(self, descriptions = "EventDescriptions.txt"):
    self.is_running = False
    self.initial_event_list = []
    self.initial_event = None
    self.additional_events = []
    self.active_events = []
    self.event_descriptions_file = descriptions
    #TODO add the main menu message
    self.main_menu_message = ""
  
  #FIXME
  def Start(self):
    if not self.is_running:
      self.Loop()
    else:
      self.active_events = []
      for event in self.additional_events:
        event.status = Status.inactive
      self.initial_event.status = Status.inactive
      self.initial_event = None
      self.Loop()
  
  def End(self):
    exit()
  
  def DisplayMenu(self, message, ):
    pass

  def RollDie(minimum, maximum):
    result = randint(minimum, maximum)
    return result
  
  def SetDescriptionLocation(self):
    filename = input("Enter location for event descriptions.")
    self.event_descriptions_file = filename
  
  def Loop(self):
    self.DisplayMenu()
    #TODO get input, begin loop

  #FIXME
  def SetEvents(self):
    pass

  def GetDescriptions(self):
    try:
      f = open(self.event_descriptions_file)
    except:
      raise Exception(f"File {self.event_descriptions_file} not found.")

    all_lines = f.readlines()

    for line in all_lines:
      if line[0:3] == "Name":
        name = line[6:]
      elif line[0:10] == "Description":
        description = line[13:]
      elif line[0:12] == "Best Practice":
        best_practice = line[15:]
        event = Event(name, description, best_practice)
        if use == "initial":
          self.initial_event_list += event
        elif use == "additional":
          self.additional_events += event
        else:
          raise Exception("Event use (initial/additional) not set properly")
      else:
        use = line.lower() if line.lower() == "initial" or line.lower() == "additional" else None

  #TODO Finish filling out TableTopGame class

# Scenario class, this class should have a name and a description of the scenario and its best practice solution.
# It should also have a markers for inactive -> active -> deactivated
#FIXME
class Event:
  def __init__self(self, name, description, best_practice):
    self.name = name
    self.description = description
    self.status = Status.inactive
    self.best_practice = best_practice
    
  def UpdateStatus(self):
    if self.status == Status.completed:
      return
    elif self.status == Status.inactive:
      self.status = Status.active
    elif self.status == Status.active:
      self.status = Status.completed
    else:
      raise Exception(f"Event status for {self.name} not properly set.")
