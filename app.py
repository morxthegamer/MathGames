from frame import Frame
import sys, os

class App:
  def __init__(self):
    self.app = Frame()
    self.unsafe_methods = ["login", "request", "setup", "save_game_iq"]
    self.methods = ["introduction", "check_iq", "change_difficulty", "sign_up", "delete_account", "start"]

  def startup(self):
    print("What would you like to do?\n")
    print("Avaliable methods:")
    for index, method in enumerate(self.methods):
      print(f"{index}. {method}")

  def unsafe(self, item):
    for method in self.unsafe_methods:
      if (item == method):
        print("Invaild option.")
        return True

  def start(self):
    os.system("cls")
    print("Welcome to The Official Math Games Terminal App!")
    while True:
      try:
        execution = input(f"{self.startup()}")
        if (execution == "."): exit(0)
        if (self.unsafe(execution)):
          continue
        exec(f"self.app.{execution}()")
      except Exception as e:
        print("Unable to execute request.\n")