# qa_python

Перечень реализованных тестов:

* Проверка на добавление двух книг. Ожидаем что в словаре будет две
  * test_add_new_book_add_two_books
* Проверка, что возможно добавить каждый из имеющихся жанров (с параметризацией)
  * test_set_book_genre_every_genre_possible_to_set[Фантастика]
  * test_set_book_genre_every_genre_possible_to_set[Ужасы]
  * test_set_book_genre_every_genre_possible_to_set[Детективы]
  * test_set_book_genre_every_genre_possible_to_set[Мультфильмы]
  * test_set_book_genre_every_genre_possible_to_set[Комедии]
* проверка, что если для книги последовательно установить два разных жанра, то в итоге остаентся именно последний
  * test_set_book_genre_set_two_genres_the_last_is_set
* Проверка, что метод `get_books_with_specific_genre` возвращает верный список книг на примере трёх книг с установленным одинаковым жанром
  * test_get_books_with_specific_genre_set_same_genre_for_three_books
* Проверка, что метод `get_books_genre` возвращает верный словарь, на примере 5 книг
  * test_get_books_genre_five_books
* Проверка, что в списке для детей только три из пяти возможных книг 
  * test_get_books_for_children_three_acceptable_for_kids
* Проверка на добавление двух книг в избранное, количество в избранном равно двум
  * test_add_book_in_favorites_add_two_books
* Проверка возможности удалить из избранного. Добавляем две, удаляем одну, ожидаем одну
  * test_delete_book_from_favorites_add_two_del_one
* Проверка корректности списка избранных. Добавили две книги, получили список, сравнили с ожидаемым
  * test_get_list_of_favorites_books_add_two_get_them_back

