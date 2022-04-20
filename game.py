import random, time, os
from termcolor import colored

class MathGames:
  def __init__(self):
    self.iq = 0
    self.wrongMessage1 = "You are incorrect. It's less than that. The answer is...{}"
    self.wrongMessage2 = "You are incorrect. It's more than that. The answer is...{}"
    self.correctMessage = "You are correct! The answer is...{}"
    self.game_message = "Math Games | Operator: {} | IQ: {} | Range: {}-{} | Mode: {}"

  def give_iq(self, op):
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

  def check_difficulty(self, difficulty, sr, er):
    if (difficulty == "EASY"):
      if (sr > 10 or er > 20):
        print("Cannot go above 1 to 20 in EASY mode.")
        exit(1)

    if (difficulty == "MEDIUM"):
      if (sr < 10 or sr > 40 and er < 20 or er > 80):
        print("Cannot go below 10 to 80 in MEDIUM mode.")
        exit(1)

    if (difficulty == "HARD"):
      if (sr < 40 or sr > 100 and er < 80 or er > 160):
        print("Cannot go below 40 to 160 in HARD mode.")
        exit(1)

    if (difficulty == "HARDER"):
      if (sr < 100 or sr > 150 and er < 160 or er > 280):
        print("Cannot go below 100 to 280 in HARDER mode.")
        exit(1)

    if (difficulty == "EXTREME"):
      if (sr < 200 or er < 320):
        print("Cannot go below 200 to 320 in EXTREME mode.")
        exit(1)

  def play(self, operator, sr, er, difficulty):
    self.check_difficulty(difficulty, sr, er)
    while True:
      print(self.game_message.format(operator, self.iq, sr, er, difficulty))
      num1 = random.randint(sr, er)
      num2 = random.randint(sr, er)
      result = eval(f"\nnum1 {operator} num2")

      play = int(input(f"\n{num1} {operator} {num2} = "))

      if play == result:
        print(colored(self.correctMessage.format(result), 'green'))
        with open("DataBase/score.yaml", "w") as f:
          self.give_iq(operator)
          f.write(f"IQ: {self.iq}")
          time.sleep(2)
          os.system("clear")
      elif result < play:
        print(colored(self.wrongMessage1.format(result), 'red'))
        break
      elif result > play:
        print(colored(self.wrongMessage2.format(result), 'red'))
        break
      else:
        print(f"You are incorrect. The answer is {result}.")
        break