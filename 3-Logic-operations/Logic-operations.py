# Ćwiczenie w którym mamy system w kinie który sprawdza czy dana osoba może wejść na film
# by wejść na flim dana osoba musi być pełnoletnia i mieć 35 zł

wiek = 9
kasa = 40


if wiek >= 18 and kasa >= 35:
    print("Można wydać bilet")
else:
    print("Biletu nie można wydać")

# operator logiczny and sprawdza czy dane dwa wejścia wiek >= 10 i kasa >=35
# są oba prawdziwe

print()
print("__________________________________________")
print()

# tym razem film jest dla dzieci i kino daje duzą wejście darmowe osobom poniżej 13 roku życia
# ten kod sprawdza czy można wydać bilet


if not wiek > 12 or kasa >= 15:
    print("Można wydać bilet")
else:
    print("Biletu nie można wydać")
# operator not odwraca wartość logiczną
# operator or sprawdza czy jakaś wartość logiczna jest równa True jeżeli tak to oddaje wartość True


####################

# operator and ma największy priorytet od operatoru or

if True or False and False:
    print("True")
else:
    print("False")

# w tym przypadku najpierw wykona się False and False co da wynik False
# a później wykona się True or False co da wynik True