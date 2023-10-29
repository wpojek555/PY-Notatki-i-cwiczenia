i = 0

# kiedy warunek i < 10 jest równy True pętla while się wykonuje
while i < 10:
    i += 1
    print(i)


print()
print("------------------------------")
print()

i = 1

# pętla z operatorem zawsze prawdziwym musi mieć metodę break by nie wykonywała się w nieskączoność
while True:
    print(i)
    i += 1
    if not i <= 10:
        break
# metoda break zatrzymuje całą pętlę

print()
print("------------------------------")
print()

# pętla która wypisze tylko liczby parzyste do 100

i = 0

while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1


print()
print("------------------------------")
print()


# pętla która wypisze liczby nieparzyste do 99

i = 0

while i <= 99:
    if i % 2 == 1:
        print(i)
    i += 1


