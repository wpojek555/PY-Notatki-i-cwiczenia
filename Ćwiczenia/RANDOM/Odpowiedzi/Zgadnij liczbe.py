# Napisz mini grę w której trzeba zgadnąć liczbę od 1 do 100

from random import randint

random = randint(0, 100)
i = 0
while True:
    a = int(input("Zgadnij liczbę: "))
    i += 1
    if a > random:
        print("Liczba jest mniejsza.")
    elif a < random:
        print("Liczba jest większa.")
    else:
        print("wygrałeś!! Zgadłeś w ", i, "próbie")
        break
