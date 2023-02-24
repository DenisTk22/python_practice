# напишите программу для печати всех уникальных значений в словаре
# list_dict = [{"V": "S001"}, {"V": "S002"},{"VI": "S001"}, {"VI": "S005"},{"VII": " S005 "}, {"V": " S009 "},{"VIII": " S007 "}]
# {'S005', 'S002', }


list_d = {}
'''
for i in list_d:
    print(list(i.values())[0].strip()) # strip чистит пробелы
'''
print(set([list(i.values())[0].strip() for i in list_d]))