from gui import GUI

class App:
  def __init__(self):
    self.app = GUI()

  def start(self):
    print("Welcome to The Official Math Games Terminal App!")
    if (sys.argv):
      for arg in sys.argv:
        self.menu(arg)

    if sys.argv[0] == "main.py" and len(sys.argv) == 1:
      while True:
        try:
          execution = input("What would you like to do?\n> ")
          exec(f"self.{execution}()")
        except Exception as e:
          print("Unable to execute request.")