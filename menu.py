def read_menu(filename='./menu.conf') -> dict:
    with open(filename, 'r') as conf:
        menu = dict()
        for line in conf:
            if line != '\n':
                item = line.replace('\n', '').split(':')
                menu[item[0]] = [item[1].strip(), item[len(item)-1].strip()]
    return menu


def show_all(dict_menu):
    for item in dict_menu:
        if str(item)[0] == '#':
            print(dict_menu[item][0])
        else:
            print(item, dict_menu[item][0])


def user_choice(dict_menu) -> str:
    index = input(f'select an action: ')
#    print(len(dict_menu))
    if len(dict_menu) > int(index) >= 1:
        result = dict_menu.get(index)[-1]
    else:
        result = 'no_operation'
#    print(result)
    return result



# menu = read_menu()
# show_all(menu)
# # print(menu)
#
# print(f'selected {user_choice(menu)}')
#
# if user_choice == 1: show_all(menu)
