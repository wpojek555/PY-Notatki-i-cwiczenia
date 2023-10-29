# w pythonie mamy listy które prszechowują wiele zmiennych

# by przypisać taką liste trzeba wykonać mniej więcej taki kod

lista = [ 1, 5, 2, 45, 10 ]

# listy mogą kośczyć się przecinkiem np:

lista = [ 1, 5, 2, 45, 10, ]

# listy mogą całe być wypisane w konsoli tak jak tutaj

print(lista)

# by wywołać dany element pojędyńczo trzeba użyć indexu

# indexy zaczynają się od 0 przykład lista[0]

# wywołanie takiego elementy wygląda tak:


print(lista[0])

# można wywołać licząc od tyłu w taki sposób

print(lista[-1])

print()
print("--------------------------")
print()

# można zmienić dany element w taki sam sposób jak zmienne tylko dodając index tego elementu

print("stara wartość", lista[3])
print("stara wartość", lista)

lista[3] = 125

print("nowa wartość", lista[3])
print("nowa wartość", lista)

print()
print("--------------------------")
print()

# listy  mogą mieć mieszane typy danych np:

lista2 = [ 241, 355.3325, "listy"]

print(lista2)


print()
print("--------------------------")
print()

# Można w typie string czyli w tekcie odwoływać się do danych liter
# Tak samo jak w listach po indexie
tekst = "Teskt"

print(tekst[0])

print(tekst[-2])

print()
print("--------------------------")
print()

print()
print()

print("Dodawanie list")
print()
print(lista + [ "f", "u" ])

print()

print("Mnożenie listy")
print()
print(lista * 3)


# Możemy wykazać ilość elementów w taki sposób
print("Ilość elementów:", len(lista))

print()

# Wkładanie objektu do środka listy
lista.insert(3, 125)
print(lista)
print()

# Liczenie Ilości danego obiektu

print("Ilość 125:", lista.count(125))

# Sprawdzanie Indexu obiektu

print()
print("Index Liczby 5:", lista.index(5))

print()
print("Usuwanie elementów z listy")
print()
lista.remove(5)
print(lista)

print()
print("Wkazywanie minimalnej i maksymalnej wartości (tylko liczby)")
print()
print("Min:", min(lista))
print("Max:", max(lista))

print()
print("Sortowanie listy:")

lista.sort()

print(lista)

print()
print("Odwracanie listy:")
print()
lista.reverse()
print(lista)
print()


print("Wyczyszczenie listy:")
print()
lista.clear()
print(lista)
