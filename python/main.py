from game import MathGames

g = MathGames(
  "Zamar",
  14,
  14921421848240
)

print(g.introduction())

print(g.check_iq())

print(g.playTheGame('*', True, 1, 10))

print(g.save_iq())