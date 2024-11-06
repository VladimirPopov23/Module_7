# module_7_1.py
# 06.11.2024 Задача "Учёт товаров"

from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name: str = name  # название продукта (строка)
        self.weight: float = weight  # общий вес товара (дробное число)
        self.category: str = category  # категория товара (строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'
    file = open(__file_name, 'a')
    file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'r')
        list = file.read()
        file.close()
        for product in products:
            if list.find(f'{product.name}') == -1:  # find возвращает индекс символа
                # , с которого начинается искомая строка, -1 в случае неудачи
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')


if __name__ == "__main__":

    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2) # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())