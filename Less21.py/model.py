def calkulator(my_list):
    while len(my_list) > 1:
        while '*' in my_list or '/' in my_list:
            i = 0
            while i < len(my_list):
                if my_list[i] == '*':
                    my_list[i - 1] = int(my_list[i - 1]) * int(my_list[i + 1])
                    del my_list[i]
                    del my_list[i]
                elif my_list[i] == '/':
                    my_list[i - 1] = int(my_list[i - 1]) / int(my_list[i + 1])
                    del my_list[i]
                    del my_list[i]
                i += 1

        while '+' in my_list or '-' in my_list:
            i = 0
            while i < len(my_list):
                if my_list[i] == '+':
                    my_list[i - 1] = int(my_list[i - 1]) + int(my_list[i + 1])
                    del my_list[i]
                    del my_list[i]
                elif my_list[i] == '-':
                    my_list[i - 1] = int(my_list[i - 1]) - int(my_list[i + 1])
                    del my_list[i]
                    del my_list[i]
                i += 1
print(calkulator)