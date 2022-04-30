from frame import Frame
import sys, os

class App:
  def __init__(self):
    self.app = Frame()
    self.unsafe_methods = ["login", "save_game_iq"]
    self.methods = [
      "introduction - Shows your stats.",
      "checkIq - Displays your current IQ Level.",
      "changeDifficulty - Change the difficulty of the game.",
      "signUp - Create a new game account.",
      "deleteAccount - Delete your account.", 
      "gameInfo - Shows info on the game.",
      "clear - Clears the screen.",
      "start - Starts the game.",
      "\'.\' - Exits the game."]

  def startup(self):
    print("What would you like to do?\n")
    print("Avaliable methods:")
    for index, method in enumerate(self.methods):
      print(f"{index}. {method}")
    return ""

  def unsafe(self, item):
    for method in self.unsafe_methods:
      if (item == method):
        print("Invaild option.")
        return True

  def start(self):
    os.system("clear")
    print("Welcome to The Official Math Games Terminal App!")
    while True:
      try:
        execution = input(f"{self.startup()}\n> ")
        if (execution == "."): exit(0)
        if (self.unsafe(execution)): continue
        exec(f"self.app.{execution}()")
      except Exception as e:
        print("Unable to execute request.\n")