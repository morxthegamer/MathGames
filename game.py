import random, time, os
from termcolor import colored

class MathGames:
  def __init__(self):
    self.iq = 0
    self.wrongMessage1 = "You are incorrect. It's less than that. The answer is...{}"
    self.wrongMessage2 = "You are incorrect. It's more than that. The answer is...{}"
    self.correctMessage = "You are correct! The answer is...{}"
    self.message = "Math Games | Operator: {} | IQ Earned: {} | Range: {}-{} | Mode: {}"

  def give_iq(self, op, difficulty):
    if (op == '+'):
      if (difficulty == "EASY"):
        self.iq += 5
      if (difficulty == "MEDIUM"):
        self.iq += 10
      if (difficulty == "HARD"):
        self.iq += 15
      if (difficulty == "HARDER"):
        self.iq += 20
      if (difficulty == "INSANE"):
        self.iq += 25
      if (difficulty == "EXTREME"):
        self.iq += 30

    if (op == '-'):
      if (difficulty == 'EASY'):
        self.iq += 6
      if (difficulty == 'MEDIUM'):
        self.iq += 12
      if (difficulty == 'HARD'):
        self.iq += 18
      if (difficulty == 'HARDER'):
        self.iq += 24
      if (difficulty == "INSANE"):
        self.iq += 30
      if (difficulty == 'EXTREME'):
        self.iq += 36

    if (op == '*'):
      if (difficulty == 'EASY'):
        self.iq += 7
      if (difficulty == 'MEDIUM'):
        self.iq += 14
      if (difficulty == 'HARD'):
        self.iq += 21
      if (difficulty == 'HARDER'):
        self.iq += 28
      if (difficulty == "INSANE"):
        self.iq += 35
      if (difficulty == 'EXTREME'):
        self.iq += 42

    if (op == '**'):
      if (difficulty == 'EASY'):
        self.iq += 10
      if (difficulty == 'MEDIUM'):
        self.iq += 20
      if (difficulty == 'HARD'):
        self.iq += 30
      if (difficulty == 'HARDER'):
        self.iq += 40
      if (difficulty == "INSANE"):
        self.iq += 50
      if (difficulty == 'EXTREME'):
        self.iq += 60

    if (op == '/'):
      if (difficulty == 'EASY'):
        self.iq += 9
      if (difficulty == 'MEDIUM'):
        self.iq += 18
      if (difficulty == 'HARD'):
        self.iq += 27
      if (difficulty == 'HARDER'):
        self.iq += 36
      if (difficulty == "INSANE"):
        self.iq += 45
      if (difficulty == 'EXTREME'):
        self.iq += 54

    if (op == '//'):
      if (difficulty == 'EASY'):
        self.iq += 8
      if (difficulty == 'MEDIUM'):
        self.iq += 16
      if (difficulty == 'HARD'):
        self.iq += 24
      if (difficulty == 'HARDER'):
        self.iq += 32
      if (difficulty == "INSANE"):
        self.iq += 40
      if (difficulty == 'EXTREME'):
        self.iq += 48

  def check_difficulty(self, difficulty, sr, er):
    if (difficulty == "EASY"):
      if (sr > 10 or er > 20):
          print("Cannot go above 1 to 20 in EASY mode.")
          exit(1)

    if (difficulty == "MEDIUM"):
      if (sr < 10 or sr > 40 and er < 20 or er > 60):
          print("Cannot go below 10 to 60 in MEDIUM mode.")
          exit(1)

    if (difficulty == "HARD"):
      if (sr < 40 or sr > 80 and er < 60 or er > 140):
          print("Cannot go below 40 to 140 in HARD mode.")
          exit(1)

    if (difficulty == "HARDER"):
      if (sr < 80 or sr > 160 and er < 140 or er > 260):
          print("Cannot go below 80 to 260 in HARDER mode.")
          exit(1)

    if (difficulty == "INSANE"):
      if (sr < 160 or sr > 240 and er < 260 or er > 320):
          print("Cannot go below 160 to 320 in HARDER mode.")
          exit(1)

    if (difficulty == "EXTREME"):
      if (sr < 400 or er < 500):
          print("Cannot go below 400 to 500 in EXTREME mode.")
          exit(1)

  def play(self, operator, sr, er, difficulty):
    self.check_difficulty(difficulty, sr, er)
    while True:
        print(self.message.format(operator, self.iq, sr, er, difficulty))
        num1, num2 = random.randint(sr, er), random.randint(sr, er)
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