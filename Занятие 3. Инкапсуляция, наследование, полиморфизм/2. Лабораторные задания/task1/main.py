class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
        self.init_name()
        self.init_author()
    def init_name(self, name):
        if not isinstance(name [str]):
            raise TypeError('Неправильный тип данных, нужен str')
    def init_author(self, author):
        if not isinstance(author [str]):
            raise TypeError('Неправильный тип данных, нужен str')

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        print('Вызван сеттер')
        self.name = value
    @property
    def author(self):
        return self.author
    @author.setter
    def author(self, value):
        print('Вызван сеттер')
        self.name = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int):
        super().__init__()
        self.pages = pages
        self.init_paperbook(pages)

    def init_paperbook(self, pages):
        if not isinstance(pages, int):
            raise TypeError('Неправильный тип данных, нужен int')

    def __str__(self):
        super(Book).__str__()
        return self.name, self.author, self.pages

    def __repr__(self):
        super(Book).__repr__()
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, duration: float):
        super().__init__()
        self.duration = duration
        self.init_audiobook(duration)

    def init_audiobook(self, duration):
        if not isinstance(duration, float):
            raise TypeError('Неправильный тип данных, нужен float')

    def __str__(self):
        super(Book).__str__()
        return self.name, self.author, self.duration

    def __repr__(self):
        super(Book).__repr__()
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration!r})"

if __name__ == "__main__":
    print('Проверка работы')
    a = PaperBook('Well', 'Done', 22)
    b = AudioBook('When', 'John', 54.3)
    print(a.__str__())
    print(a.__repr__())
    # print('               ')
    # print(b.__str__())
    # print(b.__repr__())
    #
    # print('-----------------------------------')
    #
    # print('Вызов ошибок')
    # a = PaperBook('Well', 'Done', 22.5)
    # b = AudioBook('When', 'John', 54)
    # print(a.pages)
    # print(b.duration)
