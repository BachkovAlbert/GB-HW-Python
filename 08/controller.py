import menu
import database
import operations
from os.path import isfile

def start():
    choice = menu.choice()
    
    if choice == '1':
        path = 'Phonebook_for_08.csv'
        status = isfile(path)
        if not status:
            database.create()
            print('Телефонной книги не было, создалась новая.')
        else:
            operations.show()
    
    elif choice == '2':
        result = operations.add_in_pb()
        database.writing_scv(result) 
        database.writing_txt(result)
        database.log(result)

    elif choice == '3':
        operations.re_write()
        
    elif choice == '4':
        operations.specific_show()

    else:
        print('fail') 

