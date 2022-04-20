from app import App
from threading import Thread

def main():
  game = App()
  game.start()

if __name__ == "__main__":
  thread = Thread(target=main)
  thread.start()