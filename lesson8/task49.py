#

from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    global last_id, all_data
    if last_id: 
        with open(file_base, encoding="utf-8") as f: #чтение по умолчанию
            all_data = [i.strip() for i in f]
            last_id = all_data[-1][0] #это будет работать до определенного времени. нужно split
        return all_data
    return []



def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_new_contact(): #сделать через список, Добавить проверку не существует ли такой же записи (if else) и проверка 
    global last_id
    array = ["Surname: ", "Name: ", "Patronymic: ", "Phone_number: "]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book: \n"             
                       "1. Show all records\n"      #
                       "2. Add a record\n"          #
                       "3. Search a record\n"       # разбить на две функции, берем all_data и прогоняем
                       "4. Change\n"                # проверка есть ли такая id
                       "5. Delete\n"                #
                       "6. Exp/Imp\n"               # Exp - выгрузка текущей базы в файл + расширение, Imp - изменение файл base, ввести с расширением
                       "7. Exit\n")                 # 
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                pass
            case "4":
                pass
            case "7":
                play = False
            case _:
                print("Try again\n")
main_menu()