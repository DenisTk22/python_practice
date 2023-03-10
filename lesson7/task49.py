# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
#print(*find_farthest_orbit(orbits))

def find_farthest_orbit(li):
    dict = {i[0] * i[1]: i for i in li if i[0] != i[1]}
    return max(dict.items())[1]

    
#orbits = [tuple(map(int, input().split())) for i in range(int(input('Количество орбит: ')))]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(find_farthest_orbit(orbits))

