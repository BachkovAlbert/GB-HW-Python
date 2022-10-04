import csv
import menu

def add_in_pb():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    status = False
    while not status:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                status = True
        except:
            print('Номер телефона должен состоять только из цифр')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

def show():
    with open ('Phonebook_for_08.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            print('{:<12} {:<12} {:<12} {:<12}'.format(*row))

def specific_show(): 
    last_name = input('Введите фамилию, чьи данные хотите найти: ')
    with open ('Phonebook_for_08.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            if last_name == row[0]:
                print(*row)

def delete_info(p):
    last_name = p
    temp_list = []
    with open ('Phonebook_for_08.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if last_name in item:
            temp_list.remove(item)
            print('Text deleted')          
    with open ('Phonebook_for_08.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(temp_list)
    return temp_list

def re_write():
    last_name = input('Введите фамилию, чьи данные хотите изменить: ')
    print(last_name, type(last_name))                                   #del
    temp_list = []
    with open ('Phonebook_for_08.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            temp_list.append(row)  
    for item in temp_list:
        if last_name in item:
            choice = menu.choice_re()
            if choice == '1':
                item[0] = input('Изменить фамилию на: ')
                print('Фамилия изменена.')
            if choice == '2':
                item[1] = input('Изменить имя на: ')
                print('Имя изменено.')
            if choice == '3':
                phone_number = ''
                status = False
                while not status:
                    try:
                        phone_number = input('Введите новый номер телефона: ')
                        if len(phone_number) != 11:
                            print('В номере телефона должно быть 11 цифр.')
                        else:
                            phone_number = int(phone_number)
                            status = True
                    except:
                        print('Номер телефона должен состоять только из цифр')
                item[2] = phone_number
                print('Номер телефона изменен')
            if choice == '4':
                item[3] = input('Изменить описание на: ')
                print('Имя изменено')
            if choice == '5':
                temp_list = delete_info(last_name)                        
    with open ('Phonebook_for_08.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(temp_list)