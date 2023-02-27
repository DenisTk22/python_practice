'''
Словари dict
'''

d = {'w':1, 'q':2, 'g':3}
'''
for item in d:
    print(item) # выведутся ключи: w, q, g

for item in d:
    print('wer') # выведетмя значение wer в количестве элементов в словаре - 3 раза

print(d.items()) # выведутся все элементы

x = d['w']
print(x)   # выведется значение по ключу w - wer

for k, v in d.items():
    print(k,v)         # выведет все ключи и значения

x = d.keys()
print(x)               # выведет все ключи

for i in d:
    print(i, d[i])     # выведет все ключи и значения

sum = 0
for i in d:
    sum = sum + d[i]
print(sum)
'''
'''
Строки str
'''
'''
'''
'''
w = 'лето'
sum = 0
for i in w:
    sum = sum + w[i]
print(w[0])
'''

'''
keys = [keys.append(i) for i in abc] 
values = [values.append(abc[i]) for i in abc]
'''


list_a = []
n = 4
for i in range(n):
    list_a.append(input('Ведите число: '))
print('list_a:')
print(min(list_a), max(list_a))
print(int(min(list_a)), int(max(list_a)))
print('*****')

print('list_b:')
list_b = [2, 124, 50, 300]
print(min(list_b), max(list_b))
print('*****')    