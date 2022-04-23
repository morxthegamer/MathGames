from game import MathGames
from data import Data
from IPython.display import display, Markdown
import random, json, os, time

class Help:
  def __init__(self):
    pass

  def request(self):
    os.system("clear")
    operator = input("Time to play!\nChoose an operator:\n> ")
    first, last = input("Choose a range: ").split(", ")
    first, last = int(first), int(last)
    return operator, first, last

  def setup(self):
    os.system("clear")
    while (True):
      difficulty = input(f"Please select a difficulty:\n{self.difficulties}\n> ")

      if (difficulty not in self.difficulties):
        print("Invalid Choice.")
        continue

      age = input("Please enter your age: ")
      estimated_iq = input("How much IQ you think you got?\n> ")
      break

    return difficulty, age, estimated_iq

  def login(self):
    os.system("clear")
    username = input("Please enter your username: ")
    password = input("Please enter you password: ")

    information = self.user_data.getDataJson(f"user[{username}].json")

    if (information["Username"] != username):
      print("Login failed. Wrong Username. Please try again.")
      exit(1)

    if (information["Password"] != password):
      print("Login failed. Wrong Password. Please try again.")
      exit(1)

    if (information["Username"] == username and information["Password"] == password):
      print("Successfully logged in!")
        
    return information

  def save_game_iq(self, username):
    iq = int(self.data.getData("score.yaml")[4:])
    info = self.user_data.getDataJson(f"user[{username}].json")

    info["IQ"] = int(info["IQ"]) + iq

    self.user_data.setDataJson(f"user[{username}].json", info)
    self.data.setData("score.yaml", "IQ: 0")

class Frame(Help):
  def __init__(self):
    self.game = MathGames()
    self.difficulties = ["EASY", "MEDIUM", "HARD", "HARDER", "INSANE", "EXTREME"]
    self.user_data = Data("DataBase/users")
    self.data = Data("DataBase")
    self.info = Data('')

  def introduction(self):
    print("Please Login.")
    info = self.login()
    print(
      f"""
      Name: {info["Username"]}
      Age: {info["Age"]}
      Estimated-IQ: {info["Estimated-IQ"]}
      Let's see your IQ skills.
      """
    )

  def checkIq(self):
    print("Please Login.")
    iq = self.login()["IQ"]
    print(
      f"""
      \nYour IQ Level is: {iq}!
      Congrats!
      """
    ) if (iq >= 100) else f"\nYour IQ Level is: {iq}."

  def changeDifficulty(self):
    os.system("clear")
    confirmation = input("Are you sure you want to change your difficulty? (y/n): ")
    if (confirmation == "y"):
      print("Please Login.")
      info = self.login()

      print("Your current mode is: {}.".format(info["Difficulty"]))
      new_difficulty = input(f"Enter a new difficulty:\n{self.difficulties}\n> ")

      info["Difficulty"] = new_difficulty
      self.user_data.setDataJson("user[{}].json".format(info["Username"]), info)

      print("Your new difficulty has been saved!")

  def signUp(self):
    os.system("clear")
    username = input("Please enter your username: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    for file in os.listdir("DataBase/users"):
      filename = file[5:-6]
      if (filename == username):
        print("This username is already taken. Please try again.")

    user = {"Username": username, "Email": email, "Password": password, "IQ": 0}
    user["Difficulty"], user["Age"], user["Estimated-IQ"] = self.setup()

    self.user_data.setDataJson(f"user[{username}].json", user)

  def deleteAccount(self):
    os.system("clear")
    print("Please login.")

    info = self.login()
    confirmation = input("Are you sure you want to delete your account? (y/n): ")

    if confirmation == "y":
      reason = input("Please tells us why:\n> ")
      os.remove("DataBase/users/user[{}].json".format(info["Username"]))
      print(f"Account successfully deleted. With reason:\n\n{reason}.")

  def clear(self):
    print("Clearing Screen.")
    time.sleep(1)
    os.system("clear")

  def gameInfo(self):
    print("Getting Game Data...")
    os.system("clear")
    data = self.info.getFileData("readme.md")
    print(display(Markdown(data)))

  def start(self):
    information = self.login()
    op, start, end = self.request()

    os.system("clear")
    self.game.play(op, start, end, information["Difficulty"])

    self.save_game_iq(information["Username"])