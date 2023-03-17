import json
from os import system
import time
import View


def read():
    try:
        with open('phoneBook.json', 'r', encoding="utf-8") as data:
            book = json.loads(data.read())
        return book
    except:
        return []

def save(book):
    with open('phoneBook.json', 'w', encoding="utf-8") as data:
        json.dump(book, data, indent=4, ensure_ascii=False)

def create_contact(book):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    num_tel = input("Введите телефон: ")
    contact = {"Last_name": last_name, "First_name": first_name,
               "Patronymic": patronymic, "Telefon": num_tel}
    book.append(contact)
    book = sort(book)
    save(book)
    print('\nКонтакт создан')
    return book

def update_contact(book):
    print("\nПросмотрите контакты и после введите номер контакта для обновления\n")
    time.sleep(1)
    View.view(book)
    contact_change = input("Введите номер контакта для обновления: ")
    if contact_change.isdigit() and int(contact_change) <= len(book):
        contact_change = int(contact_change)
        system("CLS")
        print("Выберите: 1.  Изменить фамилию 2. Изменить имя. 3. Изменить отчество 4. Изменит телефон")
        num = input()
        if num.isdigit()and (1 <= int(num) <= 4):
            num = int(num)
            if num == 1:
                book[contact_change-1]["Last_name"] = input(f"Введите фамилию пользователя {contact_change}: ")
            if num == 2:
                book[contact_change-1]["First_name"] = input(f"Введите имя пользователя {contact_change}: ")
            if num == 3:
                book[contact_change-1]["Patronymic"] = input(f"Введите отчество пользователя {contact_change}: ")
            if num == 4:
                book[contact_change-1]["Telefon"] = input(f"Введите новый номер телефона пользователя {contact_change}: ")
        save(book)
        print(f"\nКонтакт {contact_change} изменен")
    else:
        system("CLS")
        print("В книге нет такого контакта")
    return book


def del_contact(book):
    print("\nПросмотрите контакты и после введите номер контакта для удаления\n")
    time.sleep(1)
    View.view(book)
    num_contact = input('Какой номер контакта удалить?: ')
    if num_contact.isdigit() and int(num_contact) <= len(book):
        book.pop(int(num_contact)-1)
        save(book)
        print('\nКонтакт удален')
    else:
        print("Неверно введен номер контакта")        
    return book


def sort(book):
    lst = []
    book_sort = []
    for note in book:
        lst.append([note['Last_name'], note['First_name'],
                   note["Patronymic"], note["Telefon"]])
    lst.sort()
    for note in lst:
        book_sort.append(
            {"Last_name": note[0], "First_name": note[1], "Patronymic": note[2], "Telefon": note[3]})
    return book_sort


