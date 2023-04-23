
def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array


def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')


def show_all_items(data_array):
#    data_array = read_file(filename)
    for i in range(1,len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])


def add_item(data_array, lastname = '', firstname = '', secondname = '', phone = ''):
#    data_array = read_file(filename)
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    return data_array


def change_item(data_array):
    id = input('Введите ID шзменяемой записи: ')
    changed_item = []
    for item in data_array:
        if item[0] == id:
            changed_item = item
    changed_item[1] = input('Фамилия: ')
    changed_item[2] = input('Имя: ')
    changed_item[3] = input('Отчество: ')
    changed_item[4] = input('Телефон: ')
    return data_array

def delete_item(data_array):
    id = input('Введите ID удаляемой записи: ')
    for i in range(len(data_array)):
        if data_array[i][0] == id:
            data_array.pop(i)
    return data_array
