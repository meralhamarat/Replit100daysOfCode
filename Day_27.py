import random, os, time
def rollDice(side):
  result = random.randint(1,side)
  return result
def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat
