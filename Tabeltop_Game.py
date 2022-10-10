# This file will hold the game and scenario classes
#FIXME Game does not add events back into their respective list after a round has been played
# This means that the successive rounds will eventually crash the game.

from enum import Enum
from random import randint
from os import system

class Status(Enum):
  inactive = 0
  active = 1
  completed = 2

class Difficulty(Enum):
  debug = 0
  easy = 1
  moderate = 2
  hard = 3

def wait():
  print()
  _ = input('Press [ENTER] to continue . . . ')
  return

def clear():
  system('clear')
  return

# TableTopGame class, this class should have start, and end methods, a list containing all currently active scenarios, a roll_dice method, 
# and a count of the total number of dice rolls
class TableTopGame:
  def __init__(self, descriptions = "EventDescriptions.txt", difficulty=Difficulty.easy):
    self.is_running = False
    self.initial_event_list = []
    self.initial_event = None
    self.additional_event_list = []
    self.completed_event_list = []
    self.active_events = []
    self.event_descriptions_file = descriptions
    self.main_menu_message = "Welcome to your tabletop game.\nPlease choose an option below."
    self.num_dice_rolls = 0
    self.difficulty = difficulty
  
  #FIXME
  def Start(self):
    if not self.is_running:
      self.is_running = True
      self.Run()
    else:
      # self.active_events.clear() May not be necessary
      for event in self.completed_event_list:
        if event.use == 'initial':
          self.initial_event_list.append(event)
          event.status = Status.inactive
        elif event.use == 'additional':
          self.additional_event_list.append(event)
          event.status = Status.inactive
      self.initial_event.status = Status.inactive
      self.initial_event = None
      self.num_dice_rolls = 0
      self.Run()
  
  def ChangeDifficulty(self):
    clear()
    selection = input('Select a difficulty level (1, 2, 3): ')
    while not selection in ('1', '2','3'):
      clear()
      selection = input(f'Selection {selection} not recognized. Please try again (1, 2, 3): ')
    diff = Difficulty.easy if selection == '1' else Difficulty.moderate if selection == '2' else Difficulty.hard if selection == '3' else None
    self.difficulty = diff

  def End(self):
    clear()
    exit(0)
  
  #TODO finish displaying the full menu.
  def DisplayMenu(self, events=None, start_menu=False):
    clear()
    message = self.main_menu_message
    if start_menu:
      clear()
      print(message + '\n\n')
      print(f'1. Start game with random initial event.\n2. Choose initial event and start game.\n3. Select difficulty\n4. Exit\n\n')
    else:
      while self.active_events:
        clear()
        for event in events:
          print(f'{event.name}: {event.description}\n')
        print('Discuss and determine the best solution to the above situations.\nIf you have already discussed a solution to a problem, determine the best next step when your best practice fails.')
        wait()
        clear()
        print('Best Prcatices: \n')
        for event in events:
          event.DisplayBestPractices()
        wait()
        for event in events:
          if event == self.initial_event:
            #FIXME Add a check for debug difficulty
            if self.RollDie() > (25 * self.difficulty.value):
              self.CompleteEvent(event)
              clear()
              print(f'You have successfully completed this scenario\'s initial incident ({self.initial_event.name})')
              if self.active_events:
                print('All that remains now is to complete any remaining incidents.')
              wait()
              clear()
              # event.DisplayBestPractices()
            else:
              clear()
              print(f'Your most recent solution for the incident {event.name} has failed to resolve the issue.')
              print('You should begin considering fall-back solutions for this incident.')
              wait()
          else:
            if self.RollDie() > 10 * self.difficulty:
              self.CompleteEvent(event)
              clear()
              print(f'Your solution successfully completed the event {event.name}.\nYou will no longer have to deal with this problem')
              wait()
              clear()
            else:
              clear()
              print(f'Your most recent solution for the incident {event.name} has failed to resolve the issue.')
              print('You should begin considering fall-back solutions for this incident.')
              wait()
          if self.active_events and self.RollDie() > 70:
            if len(self.active_events) + len(self.completed_event_list) < 4:
              new_event = self.additional_event_list[randint(0, len(self.additional_event_list))]
              self.UpdateEvent(new_event)
              clear()
              print('A new incident has occured and will be ongoing until the issue is resolved.')
              print(f'You will see a description of this new incident ({event.name}) on the next screen\n\n')
              wait()

  #Return a random integer between two given values
  def RollDie(self):
    result = randint(1, 100)
    self.num_dice_rolls += 1
    return result
  
  def SetDescriptionLocation(self):
    filename = input("Enter location for event descriptions.")
    self.event_descriptions_file = filename
  
  def Run(self):
    self.DisplayMenu(start_menu=True)
    user_input = input('Selection: ')
    while not user_input in ('1', '2', '3', '4'):
      self.DisplayMenu(start_menu=True)
      user_input = input('Input not recognized. Try again: ')
    if user_input == '1':
      #Set the initial event to be equal to a random event from the initial event list, update the status of the event
      self.initial_event = self.initial_event_list[randint(0, len(self.initial_event_list) - 1)]
      self.UpdateEvent(self.initial_event)
      self.DisplayMenu(events=self.active_events)
    elif user_input == '2':
      event = self.UserSelectInitialEvent()
      self.initial_event = event
      self.UpdateEvent(self.initial_event)
      self.DisplayMenu(events=self.active_events)
    elif user_input == '3':
      self.ChangeDifficulty()
      self.initial_event = self.initial_event_list[randint(0, len(self.initial_event_list) - 1)]
      self.UpdateEvent(self.initial_event)
      self.DisplayMenu(events=self.active_events)
    else:
      self.End()

  #Update the status of an event, update self.active_events accordingly
  def UpdateEvent(self, event):
    event.UpdateStatus()
    if event.status == Status.active:
      if event.use == 'initial':
        self.initial_event_list.remove(event)
      elif event.use == 'additional':
        self.additional_event_list.remove(event)
      else:
        raise Exception(f'Event ({event.name}) did not have a use set to \'initial\' or \'additional\'')
      self.active_events.append(event)
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
        best_practice = line[15:].replace('\n', '').split(',')
        event = Event(name, description, best_practice, use)
        if use == "initial":
          self.initial_event_list.append(event)
        elif use == "additional":
          self.additional_event_list.append(event)
        else:
          raise Exception("Event use (initial/additional) not set properly")
      else:
        use = line.lower().replace('\n', '') if line.lower().replace('\n', '') == "initial" \
          or line.lower().replace('\n', '') == "additional" else None

  def UserSelectInitialEvent(self):
    clear()
    print('Initial Events:')
    options = []
    for i, event in enumerate(self.initial_event_list):
      print(f'{i + 1}: {event.name}')
      options.append(str(i + 1))
    selection = input(f'\nSelect an event: ')
    while not selection in options:
      for i, event in enumerate(self.initial_event_list):
        print(f'{i}: {event.name}')
      selection = input(f'\nSelection {selection} not recognized. Try again: ')
    index = int(selection) - 1
    return self.initial_event_list[index]
    

  def CompleteEvent(self, event):
    if not event in self.active_events:
      raise Exception(f'Event ({event.name}) not found in active events\n{self.active_events}')
    self.UpdateEvent(event)
    self.completed_event_list.append(event)

  #TODO Finish filling out TableTopGame class


# Scenario class, this class should have a name and a description of the scenario and its best practice solution.
# It should also have a markers for inactive -> active -> deactivated
#FIXME
class Event:
  def __init__(self, name, description, best_practices, use):
    self.name = name
    self.description = description
    self.status = Status.inactive
    self.best_practices = best_practices
    self.use = use
    
  def DisplayBestPractices(self):
    print(f'{self.name}:')
    for practice in self.best_practices:
      print(practice)
    return

  def UpdateStatus(self):
    if self.status == Status.completed:
      raise Exception(f'Event ({self.name}) already completed')
    elif self.status == Status.inactive:
      self.status = Status.active
    elif self.status == Status.active:
      self.status = Status.completed
    else:
      raise Exception(f"Event status for {self.name} not properly set.")

#TODO
def PlayGame(event_locations="EventDescriptions.txt", difficulty=1):
  #TODO determine different weights for dice rolls based on difficulty
  game = TableTopGame(event_locations, difficulty)
  game.GetDescriptions()
  game.Start()
  clear()
  user_response = input('Would you like to play again? (y/n): ').lower()
  while not user_response.lower() in ('y', 'n'):
    clear()
    print(f"Your input ({user_response}) was not recognized.")
    user_response = input(f'Please enter \'y\' or \'n\': ')
  while user_response == 'y':
    game.Start()
    clear()
    user_response = input('Would you like to play again? (y/n): ').lower()
  else:
    game.End()

if __name__ == '__main__':
  PlayGame()