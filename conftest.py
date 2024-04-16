import pytest
from main import BooksCollector


@pytest.fixture
def books_collector():
    return BooksCollector()
@pytest.fixture
def book_name():
    book_name = "Book1"
    return book_name

