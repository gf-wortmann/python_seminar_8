# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import menu
import data

datafile = 'phones.dat'

this_menu = menu.read_menu()
this_data = data.read_file(datafile)
menu.show_all(this_menu)
user_choice = menu.user_choice(this_menu)

while user_choice.lower() != 'exit'.lower():
    if user_choice.lower() == 'show_all'.lower():
        data.show_all_items(this_data)
    elif user_choice.lower() == 'add_record'.lower():
        this_data = data.add_item(this_data)
        data.write_file(datafile, this_data)
    elif user_choice.lower() == 'change_record'.lower():
        data.show_all_items(this_data)
        this_data = data.change_item(this_data)
        data.write_file(datafile, this_data)
    elif user_choice.lower() == 'delete_record':
        data.show_all_items(this_data)
        this_data = data.delete_item(this_data)
        data.write_file(datafile, this_data)

    menu.show_all(this_menu)
    user_choice = menu.user_choice(this_menu)

