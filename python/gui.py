from game import MathGames
import random, sys, yaml, os

class GUI:
  def __init__(self):
    self.game = MathGames()
    self.settings = []

  def getInfo(self):
    operator = input("Time to play!\nChoose an operator:\n> ")
    game_range = input("Choose a range: ")
    first, last = game_range.split(" ")
    first, last = int(first), int(last)
    return operator, first, last

  def start(self):
    print("Welcome to The Official Math Games Terminal App!")
    if (sys.argv):
      for arg in sys.argv:
        self.setting(arg)

  def setup(self): pass

  def login(self):
    email = input("Please enter your email: ")
    password = input("Please enter you password: ")
    getId = input("Please enter your id: ")

    with open(f"DataBase/users/user{getId}.yaml", "r") as f:
      info = f.readlines()
      info[0] = info[0][7:-1]
      info[1] = info[1][10:-1]
        
      if (info[0] != email):
        print("Login failed. Wrong Email. Please try again.")

      if (info[1] != password):
        print("Login failed. Wrong Password. Please try again.")

      if (info[0] == email and info[1] == password):
        print("Successfully logged in!")

  def signup(self):
    random_user_id = random.randrange(100, 999)
    username = input("Please enter your username: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    user = {
      "Username": username,
      "Email": email,
      "Password": password
    }

    with open(f"DataBase/users/user{random_user_id}.yaml", "w") as s:
      s.write(yaml.dump(user))
      print(f"Successfully signed up! Your ID is: {random_user_id}.")

  def deleteAccount(self):
    info = input("Are you sure you want to delete your account? (y/n)\n> ")
    if (info == "y"):
      reason = input("Please tell us why you want to delete your account:\n>")
      getId = input("Please enter your ID: ")
      os.remove(f"DataBase/users/user{getId}.yaml")
      print(f"Successfully deleted your account! With reason:\n{reason}.")

  def setting(self, argument):
    if argument == "-l":
        self.login()
    
    if argument == "-s":
        self.signup()

    if argument == "-p":
      op, start, end = self.getInfo()
      self.game.playTheGame(op, start, end)

    if argument == "-d":
      self.deleteAccount()