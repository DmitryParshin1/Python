def rep_list():
    my_list = my_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').\
    replace('/', ' / ').split()
    return my_list



def calculate(operation_1, operation_2):
    operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,}

    global my_list
    my_list = 0
    i = 0
    while operation_1 in my_list or operation_2 in my_list:
            if my_list[i] in [operation_1, operation_2]:
                my_list[i - 1] = operation.get(my_list[i])(int(my_list[i - 1]))(int(my_list[i + 1]))
                del my_list[i]
                del my_list[i]
            else:
                i += 1

    while len(my_list) > 1:
        calculate('*', '/')
        calculate('+','-')
    return my_list
