BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:# TODO написать класс Book
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return str(f'Книга "{self.name}"')

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books):
        self.books = books

    def get_next_book_id(self, value: int):
        append_book = Book(value)
        if self.books is None:
            self.books = append_book
        else:
            last_book = self.get_index_by_book_id(self.len - 1)
            self.library_with_books(last_book, append_book)
        self.len += 1


    def get_index_by_book_id(self, index: int) -> Book:
        if not isinstance(index,int):
            raise TypeError('Неверный тип индекса')

        if index == None:
            raise ValueError("Книги с запрашиваемым id не существует")

        current_book = self.books
        for _ in range(index):
            current_book = current_book.next
        return current_book

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
