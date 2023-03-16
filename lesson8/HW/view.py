# переменные:
last_id = 0
all_data = []
file_base = "file.txt"
from tabulate import tabulate
from os import path

# Вывод данных:


def show_all():
    if all_data: #если в all_data что-то есть (true), то выводи, если нет (false), то else
        print(*all_data, sep="\n")
    else:
        print("Empty data")

# Получение данных:

def add_new_contact(): #сделать через список, Добавить проверку не существует ли такой же записи (if else) и проверка 
    global last_id 
    array = ["Surname", "Name", "Patronymic", "Phone_number", "Comment"]
    string = ""
    for i in array:
        string += input(f"Enter {i} please: ") + " "
    last_id += 1
    #all_data.append(string)
    print()
    print(f"{last_id}  {string}")
    #print(tabulate([string], headers=["Id", "Surname", "Name", "Patronymic", "Phone_number", "Comment"], tablefmt='orgtbl')) #tablefmt='orgtbl'

    # with open(file_base, "a", encoding="utf-8") as f:
    #     f.write(f"{last_id} {string}\n")

add_new_contact()

#show_all()