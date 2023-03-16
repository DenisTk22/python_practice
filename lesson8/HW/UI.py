
from tabulate import tabulate

def new_contact():
    contact = {'id': ''}
    contact['surname'] = input('Input surname: ')
    while contact['surname'] == '':
        contact['surname'] = input('Surname is mandatory: ')
    contact['name'] = input('Input name: ')
    while contact['name'] == '':
        contact['name'] = input('Name is mandatory: ')
    contact['patronymic'] = input('Input patronymic or press "Enter" to stay empty: ')
    contact['phone'] = input('Input phone number: ')
    while contact['phone'] == '':
        contact['phone'] = input('Phone number is mandatory: ')
    contact['comment'] = input('Write a comment or press "Enter" to stay empty: ')
    print(contact)
    return contact


def show_all_data(data):
    data_to_show = []
    data_to_print = []

    for i in range(len(data)):
        li = list(data[i].values())
        li.pop(0)
        data_to_print.append(li)

    params = ["Surname", "Name", "Patronymic", "Phone number", "Comment"]
    print(data_to_print)
    print(tabulate(data_to_show, headers=params, tablefmt="fancy_grid", showindex="never"))

def search_contact():
    print("Your can search a contact by surname, name or phone number")
    search_by = input("Input here: ")
    return search_by

new_contact()

show_all_data(data)

search_contact()

