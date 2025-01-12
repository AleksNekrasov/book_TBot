import os
import sys

from database.database import users_db

"""Для того, чтобы было удобно работать с книгой -
нам нужно преобразовать текстовый файл книги в словарь,
где ключами будут номера страниц, а значениями - тексты этих страниц. """

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1450

book: dict[int: str] = {}

# функция возврата страницы книги
def book_page(user_id):
    return book[users_db[user_id]['page']]

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:

    e_o_f = len(text)  # длина текста
    if size + start + 1 >= e_o_f:
        return text[start:], len(text[start:])

    punctuation = ['.', ',', '!', ':', ';', '?']
    full_text = text
    my_text = full_text[start:size + start]

    # если последний символ из пунктуации и следом тоже..
    if full_text[start + size - 1] in punctuation and full_text[start + size] in punctuation:
        # цикл чтобы создать новый my_text без знака в конце
        for i in range(len(my_text) - 1, 0, -1):
            if my_text[i] not in punctuation:
                my_text = my_text[:i]
                break

    for i in range(len(my_text) - 1, 0, -1):
        if my_text[i] in punctuation:
            my_text = my_text[:i + 1]
            break

    return my_text, len(my_text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    global book  # Используем глобальную переменную book
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()  # Считываем весь текст книги

    start = 0
    page_number = 1  # Нумерация страниц начинается с 1

    while start < len(text):
        # Получаем текст страницы и её реальный размер
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        # Удаляем лишние символы с начала текста
        page_text = page_text.lstrip()
        # Записываем страницу в словарь
        book[page_number] = page_text
        # Увеличиваем текущее смещение
        start += page_size
        # Увеличиваем номер страницы
        page_number += 1

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
