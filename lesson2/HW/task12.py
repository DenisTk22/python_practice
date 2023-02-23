# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
d = int(s*s - 4 * p)
if d >= 0 and s <= 2000 and (math.sqrt(d)%2==0 or (math.sqrt(d)+1)%2==0):
    x = int((s + math.sqrt(d))/2)
    y = int((s - math.sqrt(d))/2)
    print('Вы загадали числа: ', x, 'и', y)
else:
    print('нет решения')
