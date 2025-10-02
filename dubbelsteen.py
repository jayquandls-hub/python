
import random

def gooi_dobbelstenen():
    return random.randint(1, 6), random.randint(1, 6)

aantal_keer = 0

while True:
    dobbelsteen1, dobbelsteen2 = gooi_dobbelstenen()

    som = dobbelsteen1 + dobbelsteen2
    aantal_keer += 1
    print(f"Worp {aantal_keer}: {dobbelsteen1} + {dobbelsteen2} = {som}")
    if som == 12:
        print(f"Het duurde {aantal_keer} worpen om 12 te gooien.")
        break
