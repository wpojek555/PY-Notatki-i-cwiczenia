print("kolejność:")
print((2 + 2) * 2)

print("dzielenie")
# zwróci liczbę float:
print(5 / 2)
# zwróci liczbę int:
print(5 // 2)

print("mnożenie:")
print(2 * 2)

print("Potęgowanie:")
print(5 ** 3)

print("Skrócone Operatory:")
x = 5
print(x)
# dodanie do zmiennej 1
x += 1
print(x)
# x++ - Błąd Inkrementacja/Dekrementacja nie działa!!!

print("Konwersja Typów:")

# funkcja input zwraca typ string

# jeżeli dodamy typ string wyjdzie nam sklejony teskt np:
# "5" + "5" = 55

# dlatego musimy przekonwertować typ string na "int" albo "float" Funkcją int / float
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
print(float(a) + float(b))

print("Usuwanie zmiennych:")

x = 15
y = 12
print(x + y)

# kiedy zmienna jest nam nie potrzebna możemy ją usunąć
del x
# ważne jest teraz by nie używać już zmiennej x ponieważ ona już nie istnieje