# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def stepen(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return stepen(a, b-1)*a

ch = int(input('Введи число: '))
st = int(input('Введи степень: '))

print(stepen(ch, st))
