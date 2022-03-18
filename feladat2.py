import math

#2.feladat
a = float(input("Adjon meg egy tört számot!"))
b = float(input("Adjon meg másik tört számot!"))
c = float(input("Adjon meg harmadik tört számot!"))

egyenlo_szaru_magassag = math.sqrt(pow(b, 2) - pow(a, 2) / 4) 

t_derek1 = a * b / 2
t_derek2 = a * c / 2
t_derek3 = b * c / 2
t_egyenlo_szaru = a * egyenlo_szaru_magassag / 2

k_derek = a + b + c
k_egyenlo_szaru = a + b * 2

if a > b + c or b > a + c or c > a + b:
    print("Nem létezik ilyen háromszög")

if pow(a, 2) + pow(b, 2) == pow(c, 2):
    print("Ez egy derékszögű háromszög")
    print(f"A háromszög kerülete: {k_derek} cm, területe: {t_derek1} cm^2")


if pow(a, 2) + pow(c, 2) == pow(b, 2):
    print("Ez egy derékszögű háromszög")
    print(f"A háromszög kerülete: {k_derek} cm, területe: {t_derek2} cm^2")

if pow(c, 2) + pow(b, 2) == pow(a, 2):
    print("Ez egy derékszögű háromszög")
    print(f"A háromszög kerülete: {k_derek} cm, területe: {t_derek3} cm^2")

if a == b:
    print("Ez egy egyenlő szárú háromszög")
    print(f"A háromszög kerülete:{k_egyenlo_szaru} cm , területe:{t_egyenlo_szaru} cm^2")
