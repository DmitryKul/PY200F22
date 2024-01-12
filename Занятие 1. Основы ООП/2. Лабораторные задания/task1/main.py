class Human:
    def __init__(self, name: str, age: int, weight: [int, float]):
        """
        Класс Человека состоит из:
        Имени - str
        Возраста - int
        Веса - float
        """
        self.name = name
        self.age = age
        self.weight = weight
    def init_name(self, name):
        """Имя человека. """
        if not isinstance(name [str]):
            raise TypeError('Неправильный тип данных, нужно str')

    def init_age(self, age):
        """Возраст человека. """
        if not isinstance(age [int]):
            raise TypeError('Неправильный тип данных, нужно int')
        if age < 0:
            raise ValueError('Возраст не должен быть меньше 0')

    def init_weight(self, weight):
        """Вес человека. """
        if not isinstance(weight [int, float]):
            raise TypeError('Неправильный тип данных, нужно int или float')
        if weight <= 0:
            raise ValueError('Вес не должен быть отрицательным или равняться 0')

class Book:
    """
    Класс Книга:
    Есть свой автор: str
    Количество страниц: int
    """
    def __init__(self, author: str, pages: int):
        self.author = author
        self.pages = pages

    def init_author(self, author):
        """Автор книги. """
        if not isinstance(author [str]):
            raise TypeError('Неправильный тип данных, нужно str')

    def init_pages(self, pages):
        """Количество страниц. """
        if not isinstance(pages [int]):
            raise TypeError('Неправильный тип данных, нужно int')
        if pages < 0:
            raise ValueError('Страниц не может быть меньше 0')
class Void:
    """
    Класс Void:
    Состоит из Ничего: None
    """
    def __init__(self):
        """В этом классе ничего нет. """
        self.void = None


# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    Guy = Human('Никита', 42, 84.5)
    print(Guy.name)# TODO работоспособность экземпляров класса проверить с помощью doctest
    print(Guy.age)
    print(Guy.weight)
    print("----------------------------------------")
    book1 = Book('А.С Пушкин', 700)
    print(book1.author)
    print(book1.pages)
    void1 = Void()
    print(void1.void is None)