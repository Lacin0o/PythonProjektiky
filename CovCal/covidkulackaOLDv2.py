from typing import Text

welcome = "Vitaj v programe Covidkulacka"
count = "Pocet nakazenych za"
day = "dni bude:"
dead = "A umrie"
ppl = "ludi,"
u2 = "dufam ze si medzi nimi aj ty."

print("\n")
print(welcome, "\n" )

while True:
    
    x = float(input("Kolko je nakazenych dnes?: " ))
    
    if x == 69:
        print("\n" "Nice" "\n" )
    
    if x >= 1000:
        print("\n" "Pokazili sme si to" "\n" )
    
    y = int(input("Pocet dni predikcie sirenia od dnes: "))
    
    if y == 22:
        print("\n" "...uz len 22 dni, prosim nezabudni...""\n")
        
    if x == 9 and y == 11:
        print("\n" "9/11 Was an Inside Job""\n")
    
    z = float(x*(1.013**y))
    f = float(z*0.097045)
    
    f_round = round(f,2)
    z_round = round(z,2)
    
    print(count, y, day, z_round,"\n")
    print(dead, f_round, ppl, u2,"\n")
    
    while True:
        again = str(input("Spustit znovu? (y/n): "))
        if again in ("y", "n"):
            break
    
    if again == 'y':
        continue

    if again == "n":
        print("Dodrzuj ROR a zamedz sireniu nakazy.")
        break
