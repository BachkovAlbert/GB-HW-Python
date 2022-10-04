import csv

def add_in_pb():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = input('Введите номер телефона: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

def show():
    with open ('Phonebook_for_07.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            print(*row)

def specific_show():
    last_name = input('Введите фамилию, чьи данные хотите найти: ')
    with open ('Phonebook_for_07.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            if last_name == row[0]:
                print(*row)

def delete_info():
    last_name = input('Введите фамилию, чьи данные хотите удалить: ')
    temp_list = []
    with open ('Phonebook_for_07.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if last_name in item:
            temp_list.remove(item)
            print('Text deleted')          
    with open ('Phonebook_for_07.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(temp_list)