# pętla for (pętla obiektowa) odpowiada takjakby za objekty np w liście.

lista = ["pętla", "for", ]


# Dla każdego X w liście lista
# Wypisz go w konsoli
for x in lista:
    print(x)

# pętla for odrazu podstawia x jako objekt w liście
# zaczyna to robić od początku do końca

print()
print("-------------------------")
print()

# wykonanie takiej pętli np 15 razy

for x in range(15):
    print(x)

# funkcja range jest obiektem podobnym do listy
# w tym przypadku ma w sobie liczby od 0 do 14
# a sama pętla wykonała się 15 razy

print()
print("-------------------------")
print()

# funkcja range może pokazywać przedział np od 5 do 15

for x in range(5, 16):
    print(x)

print()
print("-------------------------")
print()

# Funkcja range przyjmuje też argument skoku np:

for x in range(0, 25, 2):
    print(x)

# taka pętla wypisze liczby parzyste od 0 do 25

print("-------------------------")

for x in range(1, 25, 2):
    print(x)

# taka pętla wypisze liczby nie parzyste od 0 do 25 nie licząc liczby 25.


print("-------------------------")

for x in range(0, 100, 5):
    print(x)

# wypisze tylko wielokrotność liczby 5 do 100 licząc 0

