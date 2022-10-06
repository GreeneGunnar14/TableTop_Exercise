# This file will hold the game and scenario classes

from enum import Enum
from random import randint
from os import system

class Status(Enum):
  inctive = 0
  active = 1
  completed = 2
  

# TableTopGame class, this class should have start, and end methods, a list containing all currently active scenarios, a roll_dice method, 
# and a count of the total number of dice rolls
#FIXME
class __TableTopGame:
  def __init__(self, descriptions = "EventDescriptions.txt"):
    self.is_running = False
    self.initial_event_list = []
    self.initial_event = None
    self.additional_event_list = []
    self.active_events = {}
    self.event_descriptions_file = descriptions
    #TODO add the main menu message
    self.main_menu_message = "Welcome to your tabletop game.\nPlease choose an option below."
  
  #FIXME
  def Start(self):
    if not self.is_running:
      self.Run()
    else:
      self.active_events.clear()
      for event in self.additional_events:
        event.status = Status.inactive
      self.initial_event.status = Status.inactive
      self.initial_event = None
      self.Run()
  
  def End(self):
    exit(0)
  
  #TODO finish displaying the full menu.
  def DisplayMenu(self, message=None, event=None, start_menu=False):
    system('clear')
    if not message:
      message = self.main_menu_message
    if start_menu:
      system('clear')
      print(message + '\n\n')
      print('1. Start game with random initial event.\n2. Choose initial event and start game.\n3. Exit\n\n')
    else:
      raise NotImplementedError()

  #Return a random integer between two given values
  def RollDie(minimum, maximum):
    result = randint(minimum, maximum)
    return result
  
  def SetDescriptionLocation(self):
    filename = input("Enter location for event descriptions.")
    self.event_descriptions_file = filename
  
  def Run(self):
    self.DisplayMenu(start_menu=True)
    user_input = input('Selection: ')
    while not user_input in ('1', '2', '3'):
      self.DisplayMenu(start_menu=True)
      user_input = input('Input not recognized. Try again: ')
    #FIXME This is here to test that Run and Display Menu are working
    return user_input

  #Update the status of an event, update self.active_events accordingly
  def UpdateEvent(self, event):
    event.UpdateStatus()
    if event.status == Status.active:
      self.active_events.add(event)
    elif event.status == Status.completed:
      self.active_events.remove(event)

  #Go through the events file and extract all the events
  def GetDescriptions(self):
    with open(self.event_descriptions_file, 'r') as file:
      all_lines = file.readlines()

    for line in all_lines:
      if line[0:3] == "Name":
        name = line[6:]
      elif line[0:10] == "Description":
        description = line[13:]
      elif line[0:12] == "Best Practice":
        best_practice = line[15:]
        event = __Event(name, description, best_practice)
        if use == "initial":
          self.initial_event_list.append(event)
        elif use == "additional":
          self.additional_event_list.append(event)
        else:
          raise Exception("Event use (initial/additional) not set properly")
      else:
        use = line.lower() if line.lower() == "initial" or line.lower() == "additional" else None

  def SelectInitialEvent(self):
    raise NotImplementedError()

  #TODO Finish filling out TableTopGame class


# Scenario class, this class should have a name and a description of the scenario and its best practice solution.
# It should also have a markers for inactive -> active -> deactivated
#FIXME
class __Event:
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

#TODO
def PlayGame(event_locaions="EventDescriptions.txt"):
  game = __TableTopGame(event_locaions)

