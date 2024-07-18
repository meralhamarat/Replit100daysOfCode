import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strenght():
  strenghtStat = ((rollDice(6)*rollDice(8))/2)+12
  return strenghtStat

while True:
  print("🥷🧙‍KARAKTER OLUŞTURUCU🪄🧝🏻")
  print()
  isim = input("Efsaneni isimlendir:\n")
  tur = input("Karakter Türünü Seç(İnsan, Peri, Dev, Canavar, Büyücü):\n")
  print()
  print(isim)
  print("Sağlık:", health())
  print("Güç:", strenght())
  print()
  print("İsmin efsanelerde yaşasın...⚔️⚔️⚔️")
  print()
  tekrar = input("Tekrar denemek ister misin? (Evet/Hayır):\n")
  if tekrar.lower() == "hayır":
    break
    time.sleep(1)
    os.system("cls"
