import pytest
from main import BooksCollector
from testdata import TestData


@pytest.fixture()
def bc():
    return BooksCollector()


@pytest.fixture()
def bc_with_books(bc):
    for i in range(len(TestData.books)):
        bc.add_new_book(TestData.books[i]["book"])
    return bc
