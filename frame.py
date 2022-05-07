from game import Game
from data import Data
from PIL import Image
import random, json, os, time
from tkinter import *

class Frame:
  def __init__(self):
    
    # GUI Setup
    self.window = Tk()
    self.window.geometry("400x400")
    self.window.config(bg='black')
    self.window.title('Math Games')
    self.window.resizable(False, False)

    # GUI Widget Setup
    self.title_label = Label(
      self.window,
      text="Welcome to The Math Games!",
      font=("Courier", 14, "bold"),
      bg='black',
      fg='white'
    )
    self.sign_up_button = Button(
      self.window,
      text="Sign Up",
      font=('Courier', 10, 'bold'),
      relief=GROOVE,
      bg='black',
      command=self.signUp,
      fg='white'
    )
    self.login_button = Button(
      self.window,
      text="Log In",
      font=('Courier', 10, 'bold'),
      relief=GROOVE,
      command=self.login,
      bg='white',
      fg='black'
    )
    
    # Game Setup
    self.game = Game()
    self.difficulties = ["EASY", "MEDIUM", "HARD", "HARDER", "INSANE", "EXTREME"]
    self.user_data = Data("DataBase/users")
    self.data = Data("DataBase")
    self.info = Data('')

  def login(self):
    interface = Tk()
    interface.geometry("400x400")
    interface.config(bg='black')
    interface.title('Math Games')
    interface.resizable(False, False)

    login_text = Label(
      interface,
      text='Login',
      bg='black',
      fg='white',
      font=("Courier", 14, 'bold'),
    )
    
    username = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )
    
    password = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )

    username.insert('1.0', 'Username:')
    password.insert('1.0', 'Password:')

    def getInfo():
      name, pw = username.get('1.0', 'end'), password.get('1.0', 'end')
      name, pw = name.split('\n')[0], pw.split('\n')[0]
      information = self.user_data.getDataJson(f"user[{name}].json")
  
      if (information["Username"] != name):
        print('Login Failed. Wrong Username. Please try again.')
        time.sleep(3)
        interface.destroy()
        exit(0)
        
      if (information["Password"] != pw):
        print('Login Failed. Wrong Password. Please try again.')
        time.sleep(3)
        interface.destroy()
        exit(0)
  
      if (information["Username"] == name and information["Password"] == pw):
        print('Successfully logged in!')
        time.sleep(3)
        interface.destroy()
        
      return information

    login_button = Button(
      interface,
      text='Login',
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      command=getInfo
    )

    login_text.place(x=165, y=50)
    username.place(x=140, y=100)
    password.place(x=140, y=140)
    login_button.place(x=160, y=180)
    interface.mainloop()

  def save_game_iq(self, username):
    iq = int(self.data.getData("score.yaml")[4:])
    info = self.user_data.getDataJson(f"user[{username}].json")

    info["IQ"] = int(info["IQ"]) + iq

    self.user_data.setDataJson(f"user[{username}].json", info)
    self.data.setData("score.yaml", "IQ: 0")

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
    interface = Tk()
    interface.geometry("400x400")
    interface.config(bg='black')
    interface.title('Math Games')
    interface.resizable(False, False)

    sign_up_text = Label(
      interface,
      text='Sign Up',
      bg='black',
      fg='white',
      font=("Courier", 14, 'bold'),
    )
    
    username = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )

    email = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )
    
    password = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )

    age = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )

    estimated_iq = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )

    difficulty = Text(
      interface,
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      width=15,
      height=1
    )

    username.insert('1.0', 'Username:')
    email.insert('1.0', 'Email:')
    password.insert('1.0', 'Password:')
    age.insert('1.0', 'Age:')
    estimated_iq.insert('1.0', 'Estimated IQ:')
    difficulty.insert('1.0', 'Difficulty:')

    def check():
      name, mail, pw, years, iq, diff = username.get('1.0', 'end'), email.get('1.0', 'end'), password.get('1.0', 'end'), age.get('1.0', 'end'), estimated_iq.get('1.0', 'end'), difficulty.get('1.0', 'end')

      name, mail, pw, years, iq, diff = name.split('\n')[0], mail.split('\n')[0], pw.split('\n')[0], years.split('\n')[0], iq.split('\n')[0], diff.split('\n')[0]
      
      for file in os.listdir("DataBase/users"):
        filename = file[5:-6]
        if (filename == name):
          print("This username is already taken. Please try again.")
  
      user = {"Username": name, "Email": mail, "Password": pw, "IQ": 0}
  
      if (difficulty not in self.difficulties):
        print("Invalid Choice.")
  
      user["Difficulty"], user["Age"], user["Estimated-IQ"] = diff, years, iq
      self.user_data.setDataJson(f"user[{name}].json", user)

      print("Successfully signed up!")
      interface.destroy()

    sign_up_button = Button(
      interface,
      text='Sign Up',
      bg='white',
      fg='black',
      font=('Courier', 10, 'bold'),
      command=check
    )

    sign_up_text.place(x=160, y=50)
    username.place(x=140, y=100)
    email.place(x=140, y=130)
    password.place(x=140, y=160)
    age.place(x=140, y=190)
    estimated_iq.place(x=140, y=220)
    difficulty.place(x=140, y=250)
    sign_up_button.place(x=160, y=300)

    interface.mainloop()

  def deleteAccount(self):
    os.system("clear")
    print("Please login.")

    info = self.login()
    confirmation = input("Are you sure you want to delete your account? (y/n): ")

    if confirmation == "y":
      reason = input("Please tells us why:\n> ")
      os.remove("DataBase/users/user[{}].json".format(info["Username"]))
      print(f"Account successfully deleted. With reason:\n\n{reason}.")

  def startup(self):
    self.title_label.place(x=44, y=50)
    self.sign_up_button.place(x=190, y=100)
    self.login_button.place(x=110, y=100)
    self.window.mainloop()

  def start(self):
    self.startup()
    information = self.login()
    if (information):
      op, start, end = self.game.request()
      
      os.system("clear")
      self.game.play(op, start, end, information["Difficulty"])
      
      self.save_game_iq(information["Username"])