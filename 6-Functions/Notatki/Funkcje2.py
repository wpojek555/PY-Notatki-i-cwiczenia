# można przypisać działanie funkcji innej funkcji np:

def func(x):
    return x ** 2

zmienna = func

print(zmienna(6))

# funkcja może przyjąć jako argument inną funkcję np:

def func2(f1, x):
    return f1(x) * 2

print(func2(func, 5))

# silnia np: !3 = 3 * 2 * 1

def silnia(x):
    if x == 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(5))

# rekurancja: wykonywanie tej samej funkcji w funkcji