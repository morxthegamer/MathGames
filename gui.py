from game import MathGames
import random, sys, json, os

class GUI:
  def __init__(self):
    self.game = MathGames()
    self.difficulties = ["EASY", "MEDIUM", "HARD", "HARDER", "EXTREME"]

  def introduction(self):
    print("Please Login.")
    info = self.login()
    return (
      f"""
      Name: {intro["Username"]}
      Age: {intro["Age"]}
      Estimated-IQ: {intro["Estimated-IQ"]}
      Let's see your IQ skills.
      """
    )

  def check_iq(self):
    with open("DataBase/saved.yaml" , "r") as g:
      i_q = int(g.read()[4:])
      return (
        f"""
        \nYour IQ Level is: {i_q}!
        Congrats!
        """
      ) if (i_q) >= 100 else f"\nYour IQ Level is: {i_q}."

  def request(self):
    operator = input("Time to play!\nChoose an operator:\n> ")
    game_range = input("Choose a range: ")
    first, last = game_range.split(" ")
    first, last = int(first), int(last)
    return operator, first, last

  def setup(self):
    while (True):
      difficulty = input(f"Please enter a difficulty:\n{self.difficulties}\n> ")
      if (difficulty not in self.difficulties):
        print("Invalid Choice.")
        continue
      age = input("Please enter your age: ")
      estimated_iq = input("How much IQ you think you got?\n> ")
      break

    return difficulty, age, estimated_iq

  def changeDifficulty(self):
    confirmation = input("Are you sure you want to change your difficulty? (y/n): ")
    if (confirmation == "y"):
      print("Please Login.")
      info = self.login()

      with open("DataBase/users/user[{}].json".format(info["Username"]), "w") as l:
        print("Your current mode is: {}.".format(info["Difficulty"]))
        new_difficulty = input("Enter a new difficulty: ")
        info["Difficulty"] = new_difficulty
        l.write(json.dumps(info))
        print("Your new difficulty has been saved!")

  def login(self):
    username = input("Please enter your username: ")
    password = input("Please enter you password: ")

    with open(f"DataBase/users/user[{username}].json", "r") as f:
      information = json.loads(f.read())
      
      if (info["Username"] != username):
        print("Login failed. Wrong Username. Please try again.")
        exit(1)

      if (info["Password"] != password):
        print("Login failed. Wrong Password. Please try again.")
        exit(1)

      if (info["Username"] == username and info["Password"] == password):
        print("Successfully logged in!")
        
      return information

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

    user["Difficulty"], user["Age"], user["Estimated-IQ"] = self.setup()

    with open(f"DataBase/users/user[{username}].json", "w") as s:
      s.write(json.dumps(user))
      print(f"\nSuccessfully signed up!\n\nYour email is: {email}.\nYour password is: {password}.")

  def deleteAccount(self):
    info = input("Are you sure you want to delete your account? (y/n)\n> ")
    if (info == "y"):
      reason = input("Please tell us why you want to delete your account:\n> ")
      username = input("Please enter your username: ")
      os.remove(f"DataBase/users/user[{username}].json")
      print(f"Successfully deleted your account! With reason:\n{reason}.")

  def menu(self, argument):
    if argument == "-s":
      self.signup()

    if argument == "-p":
      difficulty = self.login()["Difficulty"]
      op, start, end = self.getInfo()
      self.game.play(op, start, end, difficulty)

    if argument == "-d":
      self.deleteAccount()

    if argument == "-m":
      self.changeDifficulty()