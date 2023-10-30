# Don't repeat yourself!!!
# Don't repeat yourself!!!
# Don't repeat yourself!!!

# zaczynamy funkcję poprzez def (ang: define) i podajemy dalej nazwę funkcji i kończymy nawiasami okrągłymi
def nazwa_funkcji():
    print("funkcja!!!")

# później trzeba wywołać daną funkcję

# by wywołać funkcję pidzemy jej nazwę i nawiasy okrągłe

nazwa_funkcji()


# Funkcje mogą przyjmować wartości i na nich operować np:
def dodaj(x):
    return x + 1

# metoda return zwraca w miejsce wywołanej funkcji daną wartość

print(dodaj(5)) # output: 6

# funkcje mogę mieć w sobie wiele argumentów

def dodaj(x, y):
    return x + y

print(dodaj(5, 6))

# funkcja może mieć argument tzw domyślny czyli mieć domyślną wartość np

def dodaj(x, y = 1):
    return x + y

print(dodaj(5))
print(dodaj(5 + 5))

# kiedy funkcja nie miała zmiennej y podanej wzieła wartość domyślną czyli 1 w tym przypadku

# po argumencie domyślnym trzeba przypisywać zawsze argumenty domyślne np: def dodaj(x, y = 1, z = 10)

print()
print("-------------------------")
print()

# można też wynik funkcji przypisać do zmiennej np:
w = dodaj(2, 5)

print(w)