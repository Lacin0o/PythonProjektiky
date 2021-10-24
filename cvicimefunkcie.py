from typing import Text

def vstup(hlaska):
    vstup1 =input(hlaska)
    while not vstup1.isdigit():
        print("Zadali ste blbost")
        vstup1 =input(hlaska)

    return  int(vstup1)


def Vitajte():
    print("Vitajte v programe kalkulacka")  
    print("Pre sucet zvolte +") 
    print("Pre rozdiel zvolte "-")  
    print("Pre sucin zvolte "*")
    print("Pre podiel zvolte "/")

def plus(x,y):
    z = x + y
    print("vysledok je: ", z)
    return z
        
def minus(x,y):
    z = x - y
    print("vysledok je: ", z)
    return z

def krat(x,y):
    z = x * y
    print("Vysledok je: ", z)
    return z

def delene(x,y):
    z = x / y
    z= round(z, 2)
    print("Vysledok je: ", z)
    return z


def main():
    while True: 
    
        Vitajte()
        
        x=vstup("Zadaj prve cislo: ")
        y=vstup("Zadaj druhe cislo: ")

        op = ""

        while not op in ["+", "-","*","/"]:
            
            op = str(input("Vyber operator(+,-,*,/): "))
            
            if not op in ["+", "-","*","/"]:
                print("Prosim vyberte spravny operator")
                
            
        if op == "+":
            print("Vybrali ste operaciu sucet")
            plus(x,y)

        if op == "-":
            print("Vybrali ste operaciu rozdiel")
            minus(x,y)

        if op == "*":
            print("Vybrali ste operaciu sucin")
            krat(x,y)

        if op == "/":
            print("Vybrali ste operaciu podiel")
            delene(x,y)


        while True:
            again = str(input("Spustit znovu? (y/n): "))
            if again in ("y", "n"):
                break

        if again == "y":
            continue

        if again == "n":
            print("Dovi.")
            break
  
main()
