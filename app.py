from frame import Frame
import sys, os

class App:
  def __init__(self):
    self.app = Frame()
    self.unsafe_methods = ["login", "request", "setup", "save_game_iq"]
    self.methods = ["introduction", "check_iq", "change_difficulty", "sign_up", "delete_account", "start"]

  def getMethods(self):
    for index, method in enumerate(self.methods):
      print(f"{index}. {method}")

  def start(self):
    os.system("clear")
    print("Welcome to The Official Math Games Terminal App!")
    while True:
      try:
        execution = input(f"What would you like to do?\n{self.getMethods()}\n>")
        for method in self.unsafe_methods:
          if (execution == method):
            print("Invaild option.")
            continue
        exec(f"self.app.{execution}()")
      except Exception as e:
        print("Unable to execute request.\n")