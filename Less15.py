# alien_0 = {'colol': 'green', 'points': 5}
# alien_1 = {'colol': 'yellow', 'points': 10}
# alien_2 = {'colol': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_numbers in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[0:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

#     if alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# for alien in aliens[:7]:
#     print(alien)

# print(f" Total number of aliens: {len(aliens)}")

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# print(f" You order a pizza a {pizza['crust']} - crust pizza "
#     "with the following toppins: ")
# for topping in pizza['toppings']:
#     print(" \t" + topping)


# favorite_lanuages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for name, lanuages in favorite_lanuages.items():
#     if len(lanuages) > 1:
#         print(f"\n{name}'s favorite lanuages are: ")
#     elif len(lanuages) < 2:
#         print(f" {name} favorite language is C ")
#     for lanuage in lanuages:
#         print(f"\t {lanuage}")

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }

# for username, user_info in users.items():
#     print(f"\n Username {username} ")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\t full name: {full_name}")
#     print(f"\t location: {location}")


# people = {
#     'one': {
#         'first': 'Ivan',
#         'last': 'Ivanov',
#         'age': 20,
#         'city': 'Moscow',
#     },
#     'two': {
#         'first': 'Dmitry',
#         'last': 'Petrov',
#         'age': 25,
#         'city': 'Piter',
#     },
#     'three': {
#         'first': 'Alex',
#         'last': 'Polovin',
#         'age': 28,
#         'city': 'Kazan',
#     }
# }

# for username, info in people.items():
#     print(f" \nUserName: {username} ")
#     information = f" {info['first']} {info['last']}"
#     location = f" {info['city']} "
#     year = f" {info['age']} "

#     print(f"\t name: {information}")
#     print(f"\t location: {location}")
#     print(f"\t year: {year}")

# dog = {
#     'corgi': {
#         'name': 'up',
#         'age': 2,
#         'owner_first': 'Dmitry',
#         'owner_last': 'Polovin',
#     },
#     'dog': {
#         'name': 'fred',
#         'age': 5,
#         'owner_first': 'Alex',
#         'owner_last': 'Petrov',
#     },
#     'taksa': {
#         'name': 'bin',
#         'age': 1,
#         'owner_first': 'Ivan',
#         'owner_last': 'Ivanov',
#     }
# }

# for user, info in dog.items():
#     print(f" name: {user} ")
#     people = f" info_owner: {info['owner_first']} {info['owner_last']}"
#     info_dog = f" info_owner - name: {info['name']} age: {info['age']}"
#     print(f" \tpeople_owner {people} ")
#     print(f" \tinfo_dog {info_dog} ")
# ------------------------------------

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)   # преобразуем строки в число
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# ------------------------------------


# li = [x for x in range(1,20)]

# li = list(map(lambda x: x + 10, li))

# print(li)

# ------------------------------------

# data = list(map(int, input().split()))
# print(data)

# ------------------------------------


# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)   # преобразуем строки в число
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)




