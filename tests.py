import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, books_collector):
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.get_books_genre()) == 2

    @pytest.mark.parametrize("name", ["", "a" * 41, "Book1"])
    def test_add_new_book_boundary_conditions(self, books_collector, name):
        books_collector.add_new_book(name)
        assert (name in books_collector.get_books_genre()) == (0 < len(name) < 41)

    def test_add_new_book_already_exists(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        books_collector.add_new_book(book_name)
        assert list(books_collector.get_books_genre().keys()) == [book_name]

    def test_set_book_genre_add_genre_books(self, books_collector, book_name):
        genre = "Фантастика"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self, books_collector, book_name):
        genre = "Комедии"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_for_children_books_suitable_for_children(self, books_collector, book_name):
        genre = "Мультфильмы"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_books_for_children() == [book_name]

    def test_get_books_for_children_books_unsuitable_for_children(self, books_collector, book_name):
        genre = "Детективы"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert not books_collector.get_books_for_children() == [book_name]

    def test_add_book_in_favorites_add_books(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == [book_name]

    def test_add_book_in_favorites_already_exists(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert len(books_collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_exists_in_favorites(self, books_collector, book_name):
        books_collector.delete_book_from_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == [book_name]