
import random
# De gebruiker moet de aan kunnen geven welke tafel hij wilt oefenen
print("Welke tafel wil je oefenen?")
# de input moet gevraagd worden en in een variabele gezet
tafel= int(input())
#stel hij kiest de tafel van 6, dan wil je een loop hebben met 10 lussen, met bijv. 
teller = 1
score = 0
while teller < 11:
    keer = random.randint(1, 10)
    goedeantw = keer * tafel
    gebrantw = int(input(f"{keer} x {tafel} ="))
    if goedeantw == gebrantw:
        score += 1

    teller += 1
print(f"Je score is: {score}")