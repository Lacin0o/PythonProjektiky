from typing import Text

welcome = "Vitaj v programe Covidkulacka"
count = "Pocet nakazenych za"
day = "dni bude:"
dead = "A umrie"
ppl = "ludi,"
u2 = "dufam ze si medzi nimi aj ty."

print(welcome)

x = float(input("Kolko je nakazenych dnes?: " ))
y = int(input("Pocet dni predikcie sirenia od dnes: "))


z = float(x*(1.013**y))
f = float(z*0.097045)
f_round = round(f, 2)
z_round = round(z, 2)

print(count, y, day, z_round)
print(dead, f_round, ppl, u2)
