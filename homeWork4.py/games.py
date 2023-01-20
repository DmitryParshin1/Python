# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


print('*'*90)
print('\n')


games = list(range(1,10))

def box():
    print('-------------')
    for i in range(3):
        print("|", games[0 + i * 3], "|", games[1 + i * 3], "|", games[2 + i * 3], "|")
    print('-------------')


def inpu(player):
    while True:
        numbers = input(" Поставить "  + player + ' ? - ')
        if not (numbers in'123456789'):
            print(" Повторный ввод")
            continue
        numbers = int(numbers)
        if str(games[numbers - 1]) in 'XO':
            print(' Клетка занята ')
            continue
        games[numbers - 1] = player
        break

def qwerty():
    victory = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6), (1,5,9))
    for i in victory:
        if (games[i[0] - 1]) == (games[i[1] - 1]) == (games[i[2] - 1]):
            return games[i[1] - 1]
    else: 
        return False


def play():
    count = 0
    while True:
        box()
        if count % 2 == 0:
            inpu('X')
        else:
            inpu('O')
        if count > 3:
            win = qwerty()
            if win:
                box()
                print(win, ' Победа ')
                break
        count += 1
        if count > 8:
            box()
            print(' Ничья ')
            break

play()
