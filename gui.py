from game import MathGames
import random, sys, yaml, os

class GUI:
  def __init__(self):
    self.game = MathGames()
    self.difficulties = ["EASY", "MEDIUM", "HARD", "HARDER", "EXTREME"]

  def getInfo(self):
    operator = input("Time to play!\nChoose an operator:\n> ")
    game_range = input("Choose a range: ")
    first, last = game_range.split(" ")
    first, last = int(first), int(last)
    return operator, first, last

  def setting(self, argument):
    if argument == "-s":
        self.signup()

    if argument == "-p":
      difficulty = self.login()
      op, start, end = self.getInfo()
      self.game.playTheGame(op, start, end, difficulty)

    if argument == "-d":
      self.deleteAccount()

    if argument == "m":
      self.changeDifficulty()

  def setup(self):
    while (True):
      difficulty = input(f"Please enter a difficulty:\n{self.difficulties}\n> ")
      if (difficulty not in self.difficulties):
        print("Invalid Choice.")
        continue
      break

    return difficulty

  def changeDifficulty(self):
    current_mode = self.login()
    print(f"Your current difficulty is: {mode}.")

  def login(self):
    username = input("Please enter your username: ")
    password = input("Please enter you password: ")

    with open(f"DataBase/users/user[{username}].yaml", "r") as f:
      info = f.readlines()
      mode, name, pw = info[0][12:-1], info[3][10:-1], info[2][10:-1]
      
      if (name != username):
        print("Login failed. Wrong Username. Please try again.")
        exit(1)

      if (pw != password):
        print("Login failed. Wrong Password. Please try again.")
        exit(1)

      if (name == username and pw == password):
        print("Successfully logged in!")
        
      return mode

  def signup(self):
    username = input("Please enter your username: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    for file in os.listdir("DataBase/users"):
      filename = file[5:-6]
      if (filename == username):
        print("This username is already taken. Please try again.")
        exit(1)

    user = {
      "Username": username,
      "Email": email,
      "Password": password
    }

    user["Difficulty"] = self.setup()

    with open(f"DataBase/users/user[{username}].yaml", "w") as s:
      s.write(yaml.dump(user))
      print(f"Successfully signed up!\n\nYour email is: {email}.\nYour password is: {password}.")

  def deleteAccount(self):
    info = input("Are you sure you want to delete your account? (y/n)\n> ")
    if (info == "y"):
      reason = input("Please tell us why you want to delete your account:\n> ")
      username = input("Please enter your username: ")
      os.remove(f"DataBase/users/user[{username}].yaml")
      print(f"Successfully deleted your account! With reason:\n{reason}.")

  def start(self):
    print("Welcome to The Official Math Games Terminal App!")
    if (sys.argv):
      for arg in sys.argv:
        self.setting(arg)