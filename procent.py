from unittest import case
print(" PROCENTSOMMEN OPLOSSER ")
print("Kies het type som:")
print("1. Hoeveel is x% van y?")
print("2. x is hoeveel procent van y?")
print("3. Een getal neemt toe met x%")
print("4. Een getal neemt af met x%")
print("5. Van oud naar nieuw: procentuele toename")
print("6. Van oud naar nieuw: procentuele afname")

choice = input("Voer keuze in")
match choice:
    case"1":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x / 100 * y
        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "% = " + str(x/100) + " en " + str(x/100) + " x " + str(y) + " = " + str(answer) )
    case "2":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x / y
        print("De vraag is: hoeveel procent is " + str(x) + " van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "/" + str(y) + " = " + str(answer))
    case "3":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x * (( y / 100) + 1)
        print("De vraag is: hoeveel wordt " + str(x) + " als het toeneemt met " + str(y) + " % ? ")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(y / 100 + 1) + " x " + str(x) + " = " + str(answer))
    case "4":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = y * (1 - x / 100)
        print("De vraag is: Hoeveel wordt " + str(y) + " als het afneemt met " + str(x) + " ? ")
        print(" het antwoord is: " + str(answer))
    case "5":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (y / x - 1 + 99 )
        print("De braag is: Wat is de procentuele toename van " + str(x) + " Naar " + str(y) + " ? ")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " +str(y) + " : " + str(x) + " - 1 + 99 =" + str (answer))
    case "6":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (1 - (y / x) * 100) 
        print("De vraag is: Wat is de procentuele afname van {x} naar {y}?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + "1 - " + str(y) + " / " + str(x) + " x 100 = " + str(answer) )


