import csv

def create():
    with open ('Phonebook_for_08.csv', 'a', encoding='utf-8', newline='') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(['Фамилия', 'Имя', 'Телефон', 'Описание'])

def writing_scv(info):
    with open ('Phonebook_for_08.csv', 'a', encoding='utf-8', newline='') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(info)

def writing_txt(info):
    with open ('Phonebook_for_08.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')

def log(r):
    with open('log.csv', 'a') as data:
        data.write(f'\n{str(r)}')
      