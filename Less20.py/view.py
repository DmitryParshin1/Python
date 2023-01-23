

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить котакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']

def main_menu() -> int:
    print(' Главное меню: ')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    while True:
        try: #проверка на дурака
            choice = int(input(' Выберете пункт меню: '))
            if 0 < choice < 8:
                return choice
            else:
                print(' Введите значение от 1 до 8 ')
        except ValueError:
            print(' Введите коррректное значение ')



def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print(' Телефонная книга пуста или не открыта')
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:20} {contact[2]:20}')
# жалуется  на 26 строку
        print()


def input_error():
    print(' Ошибка! Введите корректный пункт меню \n')


def empty_request():
    print(' Искомый контакт не найден! ')
def many_request():
    print(' Найдено более одного контакта. Введите точные данные ')



def create_new_contact():
    name = input(' Введите имя и фамилию: ')
    phone = input(' Введите телефон: ')
    comment = input(' Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input(' Введите искомый элемент ')
    return find

def select_contact(message: str):
    contact = input(message)
    return contact

def delete_confirm(contact: str):
    result = input(f' Вы действительно хоитте удалить контакт {contact}? (y/n)').lower()
    if result == 'y':
        return True
    else:
        return False

def change_contact():
    print(' Введите новые данные(еслии измененя не требуется нажмите Enter) ')
    name = input(' Введите имя и фамилию: ')
    phone = input(' Введите телефон: ')
    comment = input(' Введите комментарий: ')
    return name, phone, comment


def informatoin(message):
    print(message)
