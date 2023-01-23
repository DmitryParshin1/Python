import model
import view


def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()


        match choice:
            case 1:
                model.open_file()
                view.informatoin('\nФайл успешно открыт\n')
            case 2:
                model.save_file()
                view.informatoin('\nФайл успешно сохранен\n')
            case 3:
                pb = model.get_phone_book()
                view.show_contacts(pb)
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
                view.informatoin(f'\nКонтакт успешно {new_contact[0]} создан\n')
            case 5:
                del_name = view.select_contact(' Введите удаляемый контакт: ')
                contact = model.get_contact(del_name)
                if contact:
                    confirm = view.delete_confirm(contact[0][0][0])
                    if confirm:
                        model.delete_contact(view.informatoin(f'\nФайл успешно {contact[0][0]} создан\n'))
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 6:
                name = view.select_contact(' Введите изменяемый контакт: ')
                contact = model.get_contact(name)
                if confirm:
                    changed_contact = view.change_contact()
                    model.changed_contact(contact[0][1], list(changed_contact))
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 7:
                find = view.find_contact()
                result = model.searsh_contact(find)
                view.show_contacts(result)
            case _:
                view.input_error()