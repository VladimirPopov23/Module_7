# module_7_2.py
# 07.11.2024 Задача "Записать и запомнить"
from pprint import pprint

def custom_write(file_name, strings):
    file_name = 'file_name.txt' # имя файла
    file = open(file_name, 'w', encoding = 'utf-8') # открываем файл с кодировкой 'utf-8'
    strings_positions = {} # словарь
    str_num = 0 # номер строки
    byte_start_str = file.seek(0) # байт начала первой строки
    for string in strings:
        file.write(f'{string}\n') # записываем строку из списка
        str_num += 1 # следующая строка
        key = (str_num, byte_start_str) # ключ словаря
        strings_positions[key]= string # значения словаря - записываемая строка
        byte_start_str = file.tell() # байт начала следующей строки
    file.close() # закрываем файл
    return strings_positions # возвращаем получившийся словарь


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)