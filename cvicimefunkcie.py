from time import sleep
from typing import Text



while True: 
    
    x = int(input("Zadaj prve cislo: "))
    y = int(input("Zadaj druhe cislo: "))
    op = str(input("Vyber operator(+,-,*,/): "))



    
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



    if op == "+":
        plus()

    if op =="-":
        minus()

    if op =="*":
        krat()

    if op =="/":
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
