import random, os, time

def rollDice(side):
    result = random.randint(1,side)
    return result

def health():
    healthStat = ((rollDice(6)*rollDice(8))/2)+10
    return healthStat

def strenght():
    strenghtStat = ((rollDice(6)*rollDice(10))/2)+12
    return strenghtStat

print("\033[92m⚔️ SAVAŞ ZAMANI ⚔️\033[0m")
print()
isim1 = input("Efsanenizi isimlendirin:\n")
tur1 = input("Türünü seçin(insan, Canavar, Elf, Büyücü\n")
print()
print(isim1)
c1health = health()
c1strength = strenght()
print("Sağlık:", c1health())
print("Güç:", c1strength())

print()
print("Kiminle savaşacak?")
print()

isim2 = input("Efsaneyi isimlendirin:\n")
tur2 = input("Türünü seçin(insan, Canavar, Elf,Büyücü)\n")
print()
print(isim2)
c2health = health()
c2strength = strenght()
print("Sağlık:", c2health())
print("Güç:", c2strength())
print()
round = 1
kazanan = None

while True:
    time.sleep(1)
    os.system("clear")
    print("Ve bir sonraki tur için ayakta duruyorlar")
    round -= 1
    print("\033[93m⚔️ SAVAŞ BAŞLIYORR!!!! ⚔️\033[0m")
    c1Dice = rollDice(6)
    c2Dice = rollDice(6)
    difference = (abs(c1strength-c2strength)) + 1

    if c1Dice > c2Dice:
        c2health-= difference
        if round == 1:
            print(isim1,"İlk darbeyi vuruyor\n")
        else:
            print(isim1,round,"turu kazandı\n")
    elif c1Dice < c2Dice:
        c2health -= difference
        if round == 1 :
            print(isim2, "İlk darbeyi vuruyor\n")
        else:
            print(isim2, round, "turu kazandı\n")
    else:
        print("Kılıçları çarpıştırdılar ve", round, ". turda berabere kaldılar")

    print()
    print(isim1)
    print("Sağlık:", c1health)
    print()
    print(isim2)
    print("Sağlık:", c2health)
    print()

    if c1health <= 0:
        print(isim1,"ölüyor!")
        kazanan = isim2
        break
    elif c2health <= 0:
        print(isim2,"ölüyor!")
        kazanan = isim1
        break
    else:
        print("Ve bir sonraki tur için ayakta duruyorlar")
        round += 1

time.sleep(2)
os.system("clear")
print("\033[92m⚔️ SAVAŞ ZAMANI ⚔️\033[0m")
print()
print(kazanan, "kazandı, toplamda", round, "turu")