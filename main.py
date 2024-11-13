# module_7_5.py
# 13.11.2024 Домашнее задание по теме "Файлы в операционной системе".

import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):  # цикл для обхода каталога, путь к которому указывает переменная directory
    for file in files:
        file_path = os.path.join(root, file)  # объединяет список строк root с помощью указателя file в один путь.
        file_time = os.path.getmtime(file_path)  # возвращает время последней модификации файла file_path
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(
            file_time))  # преобразует кортеж, в строку 'день.месяц.год час:минута'.
        file_size = os.path.getsize(file_path)  # размера файла.
        parent_dir = os.path.dirname(file_path)  # родительская директории файла.
        print(
            f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт,'
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
