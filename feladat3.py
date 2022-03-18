class Bolygo:
    def __init__(self, sor):
        nev, holdak, terfogat = sor.strip().split(";")
        self.nev = nev
        self.holdak = int(holdak)
        self.terfogat = float(terfogat)

with open("solsys .txt") as f:
    lista = [Bolygo(sor) for sor in f]

#3.1
print(f"3.1: {len(lista)} bolygó van a naprendszerben")

#3.2
hold = [sor.holdak for sor in lista]
atlag = sum(hold) / len(lista)
print(f"3.2: A naprendszerben egy bolygónak átlagosan {atlag} holdja van")

#3.3
legnagyobb = max([(sor.terfogat, sor.nev) for sor in lista])
print(f"3.3: A legnagyobb térfogatú bolygó a {legnagyobb[1]}")

#3.4
bekert = input("3.4: Írd be a keresett bolygó nevét:")
van_e = ""
for sor in lista:
    if bekert != sor.nev:
        van_e = "Sajnos nincs ilyen bolygó a naprendszerben"
    else:
        van_e = "Van ilyen bolygó a naprendszerben"
print(van_e)

#3.5
szam = int(input("Írj be egy számot:"))
mennyi = [sor.nev for sor in lista if sor.holdak >= szam]
print(f"A következő bolygóknak van {szam}-nál/nél több holdja:")
print(mennyi)


