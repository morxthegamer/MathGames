from tkinter import *
import random, time

class GUI:
  def __init__(self):
    self.window = Tk()
    self.window.geometry("400x400")
    self.window.config(bg='black')
    self.window.title('Math Games')
    self.window.resizable(False, False

  def start(self):
    self.title_label.place(x=44, y=50)
    self.sign_up_button.place(x=190, y=100)
    self.login_button.place(x=110, y=100)
    self.window.mainloop()

app = GUI()
app.start()