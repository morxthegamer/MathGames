from frame import Frame
import sys, os

class App:
  def __init__(self):
    self.app = Frame()

  def start(self):
    os.system("clear")
    print("Welcome to The Official Math Games Terminal App!")
    unsafe_methods = ["login", "request", "setup", "save_game_iq"]
    while True:
      try:
        execution = input("What would you like to do?\n> ")
        for method in unsafe_methods:
          if (execution == method):
            print("Invaild option.")
            continue
        exec(f"self.app.{execution}()")
      except Exception as e:
        print("Unable to execute request.\n")