#1.feladat
szam = int(input("Adjon meg egy számot!"))
szo = input("Adjon meg egy szót!")
kiiras = pow(szam, 2)

for _ in range(kiiras):
    print(szo.lower(), end=", ")


