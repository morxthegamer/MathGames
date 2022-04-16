import random
from termcolor import colored

class MathGames:
  def __init__(self, name="", age=0, est_iq=0):
    self.name = name
    self.age = age
    self.est_iq = est_iq
    self.iq = 0
    self.wrongMessage1 = "You are incorrect. It's less than that. The answer is...{}"
    self.wrongMessage2 = "You are incorrect. It's more than that. The answer is...{}"
    self.correctMessage = "You are correct! The answer is...{}"

  def introduction(self):
    intro = {
      "Name": self.name,
      "Age": self.age,
      "Estimated-IQ": self.est_iq,
    }
    return (
      f"""
      Name: {intro["Name"]}
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

  def save_iq(self):
    with open("DataBase/score.yaml", "r") as h:
      iq = int(h.read()[4:])
    with open("DataBase/saved.yaml", "r") as j:
      i = int(j.read()[4:])
    with open("DataBase/saved.yaml", "w") as o:
      o.write(f"IQ: {iq + i}")
      print("IQ saved successfully!")
    with open("DataBase/score.yaml", "w") as k:
      k.write("IQ: 0")

  def clear_iq(self):
    with open("DataBase/saved.yaml", "w") as t:
      t.write("IQ: 0")
      return "Successfully cleared all your IQ points."
  
  def check_iq_with_est_iq(self):
    msg1 = "Your Estimated IQ is lower than your actual IQ."
    msg2 = "Your Estimated IQ is higher than your actual IQ."
    with open("saved.yaml", "r") as l:
      iq = int(l.read()[4])
    return msg1 if iq < self.est_iq else msg2

  def playTheGame(self, operator, sr: int, er: int):
    def give_iq(op):
      if (op == '+'):
        self.iq += 5

      if (op == '-'):
        self.iq += 8

      if (op == '*'):
        self.iq += 12

      if (op == '**'):
        self.iq += 15

      if (op == '/'):
        self.iq += 18

      if (op == '//'):
        self.iq += 18
      
    while True:
      num1 = random.randint(sr, er)
      num2 = random.randint(sr, er)
      result = eval(f"num1 {operator} num2")

      play = int(input(f"\n{num1} {operator} {num2} = "))

      if play == result:
        print(colored(self.correctMessage.format(result), 'green'))
        with open("DataBase/score.yaml", "w") as f:
          give_iq(operator)
          f.write(f"IQ: {self.iq}")
      elif result < play:
        print(colored(self.wrongMessage1.format(result), 'red'))
        break
      elif result > play:
        print(colored(self.wrongMessage2.format(result), 'red'))
        break
      else:
        print(f"You are incorrect. The answer is {result}.")
        break