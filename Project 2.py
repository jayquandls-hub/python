import random

namen = ["Daan A.", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", 
         "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", 
         "Semen", "Ajay", "Bert", "Rogier", "Daan V.", "Kateryna"]

y = int(input("Hoeveel namen wil je? "))

if y > len(namen):
    print(f"Je kunt maximaal {len(namen)} namen kiezen.")
else:
    gekozen_namen = random.sample(namen, y)
    for naam in gekozen_namen:
        print(naam)
    