

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
        # добавить проверку на дурака
    choice = int(input(' Выберете пункт меню: '))
    return choice


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

def create_new_contact():
    name = input(' Введите имя и фамилию: ')
    phone = input(' Введите телефон: ')
    comment = input(' Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input(' Введите искомый элемент ')
    return find