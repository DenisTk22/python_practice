# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

n = int(input('Введите число для вычисления факториала: '))
count = 1
fact = 1
while count <= n:
    fact *= count
    count += 1
print("факториал = ", fact)
