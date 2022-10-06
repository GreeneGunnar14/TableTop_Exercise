# This file will hold the game and scenario classes

from enum import Enum
from random import randint
from os import system

class Status(Enum):
  inactive = 0
  active = 1
  completed = 2
  
def wait():
  _ = input('Press [ENTER] to continue . . . ')
  return
# TableTopGame class, this class should have start, and end methods, a list containing all currently active scenarios, a roll_dice method, 
# and a count of the total number of dice rolls
#FIXME
class TableTopGame:
  def __init__(self, descriptions = "EventDescriptions.txt"):
    self.is_running = False
    self.initial_event_list = []
    self.initial_event = None
    self.additional_event_list = []
    self.active_events = set()
    self.event_descriptions_file = descriptions
    self.main_menu_message = "Welcome to your tabletop game.\nPlease choose an option below."
    self.num_dice_rolls = 0
  
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
      self.num_dice_rolls = 0
      self.Run()
  
  def End(self):
    exit(0)
  
  #TODO finish displaying the full menu.
  def DisplayMenu(self, events=None, start_menu=False):
    system('clear')
    message = self.main_menu_message
    if start_menu:
      system('clear')
      print(message + '\n\n')
      print('1. Start game with random initial event.\n2. Choose initial event and start game.\n3. Exit\n\n')
    else:
      system('clear')
      for event in events:
        print(f'{event.name}: {event.description}\n')
      print('Discuss and determine the best solution to the above situations.\nIf you have already discussed a solution to a problem, determine the best next step when your best practice fails.')
      wait()
      system('clear')
      print('Best Prcatices: \n')
      for event in events:
        print(f'{event.name}: {event.best_practice}\n')
      wait()


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
    if user_input == '1':
      #Set the initial event to be equal to a random event from the initial event list, update the status of the event
      self.initial_event = self.initial_event_list[randint(0, len(self.initial_event_list) - 1)]
      self.UpdateEvent(self.initial_event)
      self.DisplayMenu(events=self.active_events)
      #TODO finish writing out code for the initial event handling
    elif user_input == '2':
      raise NotImplementedError()
      #TODO write steps for user selection of an initial event
    else:
      self.End()

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
      if line[0:4] == "Name":
        name = line[6:].replace('\n', '')
      elif line[0:11] == "Description":
        description = line[13:]
      elif line[0:13] == "Best Practice":
        best_practice = line[15:].replace('\n', '')
        event = Event(name, description, best_practice)
        if use == "initial":
          self.initial_event_list.append(event)
        elif use == "additional":
          self.additional_event_list.append(event)
        else:
          raise Exception("Event use (initial/additional) not set properly")
      else:
        use = line.lower().replace('\n', '') if line.lower().replace('\n', '') == "initial" \
          or line.lower().replace('\n', '') == "additional" else None

  def SelectInitialEvent(self):
    raise NotImplementedError()

  #TODO Finish filling out TableTopGame class


# Scenario class, this class should have a name and a description of the scenario and its best practice solution.
# It should also have a markers for inactive -> active -> deactivated
#FIXME
class Event:
  def __init__(self, name, description, best_practice):
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
def PlayGame(event_locations="EventDescriptions.txt", difficulty=0):
  #TODO determine different weights for dice rolls based on difficulty
  if difficulty == 0:
    pass
  elif difficulty == 1:
    pass
  elif difficulty == 2:
    pass
  game = TableTopGame(event_locations)
  game.GetDescriptions()
  game.Start()
  system('clear')
  user_response = input('Would you like to play again? (y/n): ').lower()
  while user_response == 'y':
    game.Start()
    system('clear')
    user_response = input('Would you like to play again? (y/n): ').lower()

if __name__ == '__main__':
  PlayGame()