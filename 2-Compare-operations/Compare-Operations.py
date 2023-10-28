print("sprawdzanie czy operatory są równe sobie: ")

print(5 == 5) # True
print(5 == 1) # False

print()
print("sprawdzanie czy operatory są różne: ")


print(5 != 1) # True
print(5 != 5) # False

print()
print("sprawdzanie czy operatory są większe/mniejsze: ")


print(5 > 1) # True
print(5 < 1) # False

print()
print("sprawdzanie czy operatory są większe/mniejsze/Równe: ")


print(5 >= 5) # True
print(5 <= 1) # False

print()
print("Instrukcja warunkowa IF:")
x = 10
y = 15

if x < y:
    print(x, "jest mniejsze od", y)
elif x > y:
    print(x, "jest większe od", y)
else:
    print(x, "jest równe", y)

