# Дан список чисел. Посчитайте,
# сколько в нем пар элементов,
# равных друг другу.

# Считается, что любые два элемента,
# равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.

list1 = [1, 9, 6, 4, 8, 9, 4, 1]

# list2 = list[set(list1)]
# print(list2)
# count = 0
# for i in range(len(list2)):
#     count += list1.count(list2[i])//2 
# print(count)

d_list = {}.fromkeys(list1, 0)
print(d_list)
for i in list1:
    d_list[i] += 1

print(sum([i//2 for i in d_list.values() if not i%2]))