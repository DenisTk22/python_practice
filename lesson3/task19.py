# дана последовательность из N целых чисел и число К.
# необходимо сдвинуть всю последовательность (сдвиг - циклический) на К элементов вправо, К - положительное число.
# 1.2.3.4.5 k=3 -> 3.4.5.1.2
listik = [1, 2, 3, 4, 5]

k = int(input('Введите число: '))

for i in range(k):
    listik.insert(0, listik.pop(-1))

print(listik)

'''
[6, 1, 2, 3, 4, 5] - 1 шаг
[5, 6, 1, 2, 3, 4] - 2 шаг
[4, 5, 6, 1, 2, 3] - 3 шаг
[3, 4, 5, 6, 1, 2] - 4 шаг
[2, 3, 4, 5, 6, 1] - 5 шаг
[1, 2, 3, 4, 5, 6] - 6 шаг
[6, 1, 2, 3, 4, 5] - 7 шаг
'''