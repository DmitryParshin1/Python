import model
import view


def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()


        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                pb = model.get_phone_book()
                view.show_contacts(pb)
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                pass
            case 6:
                pass
            case 7:
                find = view.find_contact()
                result = model.searsh_contact(find)
                view.show_contacts(result)
            case _:
                view.input_error()