#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
#разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

num = int(input('Введите количество элементов арифметической прогрессии: '))
a1 = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите разность элементов: '))
a = []
for n in range(2, num+1):
    b = a1 + (n-1)*d
    a.append(b)
a.insert(0, a1)
print(a)

#a = a.append(b = a1 + (n-1)*d n for n in range(2, num+1))