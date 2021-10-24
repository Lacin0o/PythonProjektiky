from time import sleep
from typing import Text

def vstupx():
    try:
        x = int(input("Zadaj prve cislo: "))
        print("Zadali ste ""int"" cislo:",x)
    except ValueError:
        try:
            x = float(input)
            print("Zadali ste ""float"" cislo:", x)
        except ValueError:
            print("Prosim zadajte CISLO, nie string")

def vstupy():
    try:
        y = int(input("Zadaj prve cislo: "))
        print("Zadali ste ""int"" cislo:",y)
    except ValueError:
        try:
            y = float(input)
            print("Zadali ste ""float"" cislo:", y)
        except ValueError:
            print("Prosim zadajte CISLO, nie string")

def Vitajte():
    print("Vitajte v programe kalkulacka")
    sleep(1.5)
    print("Pre sucet zvolte +")
    sleep(0.5)
    print("Pre rozdiel zvolte -")
    sleep(0.5)
    print("Pre sucet sucin *")
    sleep(0.5)
    print("Pre sucet podiel /")
    sleep(0.5)

def plus():
    z = x + y
    print("vysledok je: ", z)
        
def minus():
    z = x - y
    print("vysledok je: ", z)

def krat():
    z = x * y
    print("Vysledok je: ", z)

def delene():
    z = x / y
    print("Vysledok je: ", z)



while True: 
    
    Vitajte()
    
    vstupx()
    vstupy()

    x = ""
    y = ""
    z = ""

    
    op = ""

    while not op in ["+", "-","*","/"]:
        
        op = str(input("Vyber operator(+,-,*,/): "))
        
        if not op in ["+", "-","*","/"]:
            print("Prosim vyberte spravny operator")
            sleep(3)
        
    if op == "+":
        print("Vybrali ste operaciu sucet")
        sleep(1)
        plus()

    if op == "-":
        print("Vybrali ste operaciu rozdiel")
        sleep(1)
        minus()

    if op == "*":
        print("Vybrali ste operaciu sucin")
        sleep(1)
        krat()

    if op == "/":
        print("Vybrali ste operaciu podiel")
        sleep(1)
        delene()


    while True:
        again = str(input("Spustit znovu? (y/n): "))
        if again in ("y", "n"):
            break

    if again == "y":
        continue

    if again == "n":
        print("Dovi.")
        break
