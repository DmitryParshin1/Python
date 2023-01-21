

phone_book = []
# path = 'Less20.py/phone_book.txt'  # правой кнопкой мыши - copy relative path
path = '/Users/dimaparsin/Desktop/python/Less20.py/phone_book.txt'


def get_phone_book():
    global phone_book
    return phone_book


def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as data: # encoding='UTF-8' формат отображения печати, что вывобитна экран
        file = data.readline()
    for contact in file:
        phone_book.append(contact.strip().split(';'))


def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    # print(pb_str)
    # print('\n'.join(pb_str))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))


def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)


def searsh_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result
