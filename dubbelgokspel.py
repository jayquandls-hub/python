import random
# er moet een random getal komen tussen 1 en 6: dit getal zet ik in een worp 
worp = random.randint(1,6)
# de gebruiker moet een gok kunnen invoeren 
# Het ingevoerde getal door een gebruiker moet opgepakt worden: dit getal zet ik in gok 
gok = int(input("Gok het getal"))
# worp en gok moet vergeleken worden: als gok= worp dan "hoera" , anders "duimpje omlaag"
if worp == gok:
    print("Jij moet gaan gokken")
else:
    print("Om 1u wordt jij geblazen")   