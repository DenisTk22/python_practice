# Даны два массива чисел. Требуется вывести те
# элементы первого массива (в том порядке,
# в каком они идут в первом массиве),
# которых нет во втором массиве.

# Пользователь вводит число N - количество
# элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива

count1 = int(input('Сколько элементов будет в первом массиве? —> '))
list1 = []
for _ in range(count1):
    list1.append(int(input('\tэлемент массива —> ')))
count2 = int(input('Сколько элементов во втором массиве? —> '))
list2 = []
for _ in range(count2):
    list2.append(int(input('\tэлемент массива —> ')))

print([x for x in list1 if x not in (list2)])