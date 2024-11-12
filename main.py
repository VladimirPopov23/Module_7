# module_7_3.py
# 12.11.2024 Задача "Найдёт везде"

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names  # атрибут принимающий неограниченное кол-во названий файлов
        # file_names = name.append()

    def get_all_words(self):
        all_words = {}  # словарь для записи данных, (ключ - название файла, значение - список из слов этого файла)
        for name in self.file_names:  # цикл для того что бы перебрать названия файлов
            with open(name, 'r', encoding='utf-8') as file:  # оператор with поочередно открывает файлы в utf-8
                info = file.read().lower()  # .read() считывает файл в строку и .lower() переводит элементы в н.регистр
                for s in [',', '.', '=', '!', '?', ';', ':', ' - ']:  # цикл для поиска пунктуации в s строках файла
                    info = info.replace(s, '')  # .replace() заменяет знаки пунктуации на ничто ''
                all_words[name] = info.split()  # переписывает значение в файле name без пунктуации, но разделив .split() строку
        return all_words

    # find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        find_word = {}  # словарь, где ключ - название файла, значение - позиция первого такого слова в файле
        for name, words in self.get_all_words().items():  # цикл для поиска слов в списке слов этого файла по ключу
            if word.lower() in words:  # если слово (в н.регисте) есть в значении списка all_words (метод get_all_words)
                find_word[name] = words.index(word.lower()) + 1  # то по ключу name присваеваем words значение позиции в последовательности, c учетом, что первый эл-т - 0
                find_word.update()  # добавляем ключ/значение в словарь
        return find_word  # по завершению цикла возвращаем словарь find_word

    # count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
    def count(self, word):
        count_word = {}  # словарь, где ключ - название файла, значение - количество слов 'word' в файле
        for name, words in self.get_all_words().items():  # цикл для поиска слов в списке слов этого файла по ключу
            count_word[name] = words.count(word.lower())  # .count считает кол-во слов (в н.регисте) в списке слов файла name
        return count_word  # по завершению цикла возвращаем словарь count_word



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего