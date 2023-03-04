# Развернуть строку со значениями
# n = [1,2,3,4]
# print(n[::-1])

def r(n):
    if n == 0:
        return ''
    stroch = input()
    return r(n-1) + stroch

nums = int(input('Количество элементов'))
print(r(nums))