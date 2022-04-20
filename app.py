from gui import GUI
import sys

class App:
  def __init__(self):
    self.app = GUI()

  def start(self):
    print("Welcome to The Official Math Games Terminal App!")
    if (sys.argv):
      for arg in sys.argv:
        self.app.start(arg)

    if sys.argv[0] == "main.py" and len(sys.argv) == 1:
      while True:
        try:
          execution = input("What would you like to do?\n> ")
          if (execution == "login" or execution == "request" or execution == "setup" or execution == "save_game_iq" or execution == "start"):
            print("Invaild option.")
            continue
          exec(f"self.app.{execution}()")
        except Exception as e:
          print("Unable to execute request.")