# 2. В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрести для них.

m = int(input('колличество учеников в первом классе: '))
n = int(input('колличество учеников во втором классе: '))
k = int(input('колличество учеников в третьем классе: '))
print(-((-m//2)+(-n//2)+(-k//2)))