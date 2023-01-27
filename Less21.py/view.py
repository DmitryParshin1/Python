

def rep_list():
    my_list = my_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').\
    replace('/', ' / ').split()
print(rep_list)
