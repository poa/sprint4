from main import BooksCollector
import pytest


class TestData:
    books = [
        {"book": "Град обречённый", "genre": "Фантастика"},
        {"book": "Что делать, если ваш кот хочет вас убить", "genre": "Ужасы"},
        {"book": "Кто убил мистера Н", "genre": "Детективы"},
        {"book": "Котёнок по имени Гав", "genre": "Мультфильмы"},
        {"book": "Гордость и предубеждение и зомби", "genre": "Комедии"},
    ]


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    @pytest.fixture()
    def bc(self):
        return BooksCollector()

    @pytest.fixture()
    def bc_with_books(self, bc):
        for i in range(len(TestData.books)):
            bc.add_new_book(TestData.books[i]["book"])
        return bc

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, bc):

        # добавляем две книги
        bc.add_new_book(TestData.books[0]["book"])
        bc.add_new_book(TestData.books[1]["book"])

        # проверяем, что добавилось именно две
        assert len(bc.books_genre) == 2

    @pytest.mark.parametrize("genre", [item["genre"] for item in TestData.books])
    def test_set_book_genre_every_genre_possible_to_set(self, bc, genre):
        book = TestData.books[0]["book"]

        bc.add_new_book(book)
        bc.set_book_genre(book, genre)
        assert bc.get_book_genre(TestData.books[0]["book"]) == genre

    def test_set_book_genre_set_two_genres_the_last_is_set(self, bc_with_books):
        book = TestData.books[0]["book"]
        genre1 = TestData.books[0]["genre"]
        genre2 = TestData.books[1]["genre"]

        bc_with_books.set_book_genre(book, genre1)
        bc_with_books.set_book_genre(book, genre2)
        assert bc_with_books.get_book_genre(book) == genre2

    def test_get_books_with_specific_genre_set_same_genre_for_three_books(self, bc_with_books):
        genre = TestData.books[0]["genre"]

        for item in TestData.books[:3]:
            bc_with_books.set_book_genre(item["book"], genre)

        fiction_books = bc_with_books.get_books_with_specific_genre(genre)

        assert set(fiction_books) == set(list([TestData.books[i]["book"] for i in range(3)]))

    def test_get_books_genre_five_books(self, bc_with_books):
        expected_dict = {}

        for item in TestData.books:
            expected_dict[item["book"]] = ""

        assert set(bc_with_books.get_books_genre()) == set(expected_dict)

    def test_get_books_for_children_three_acceptable_for_kids(self, bc_with_books):
        for item in TestData.books:
            bc_with_books.set_book_genre(item["book"], item["genre"])

        assert len(bc_with_books.get_books_for_children()) == 3

    def test_add_book_in_favorites_add_two_books(self, bc_with_books):
        book1 = TestData.books[0]["book"]
        book2 = TestData.books[1]["book"]

        bc_with_books.add_book_in_favorites(book1)
        bc_with_books.add_book_in_favorites(book2)

        assert len(bc_with_books.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_add_two_del_one(self, bc_with_books):
        book1 = TestData.books[0]["book"]
        book2 = TestData.books[1]["book"]

        bc_with_books.add_book_in_favorites(book1)
        bc_with_books.add_book_in_favorites(book2)
        bc_with_books.delete_book_from_favorites(book1)

        assert len(bc_with_books.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_add_two_get_them_back(self, bc_with_books):
        book1 = TestData.books[3]["book"]
        book2 = TestData.books[4]["book"]

        bc_with_books.add_book_in_favorites(book1)
        bc_with_books.add_book_in_favorites(book2)

        assert bc_with_books.get_list_of_favorites_books() == [
            item["book"] for item in TestData.books[3:]
        ]
