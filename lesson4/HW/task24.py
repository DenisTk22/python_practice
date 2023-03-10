#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите количество кустов: '))
gryada = []
moduls = []
for i in range(n):
    gryada.append(input('Ведите число ягод на кусту: '))
print(gryada)
for i in range(n):
    if i == n - 2:
        modul = int(gryada[i]) + int(gryada[n-1]) + int(gryada[0])
    elif i == n - 1:
        modul = int(gryada[i]) + int(gryada[0]) + int(gryada[1])
    else:
        modul = int(gryada[i]) + int(gryada[i+1]) + int(gryada[i+2])
    moduls.append(modul)
print(moduls)

print('Максимально можно собрать за один проход:',max(moduls), 'ягод')
