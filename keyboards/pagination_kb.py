from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.database import users_db # добавил от себя для работы созданной ф-ии
from lexicon.lexicon import LEXICON

"""Клавиатура для пагинации"""

def _create_pagination_keyboard(*buttons: str) ->InlineKeyboardMarkup:

    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(
        *[InlineKeyboardButton(
            text=LEXICON[button] if button in LEXICON else button,
            callback_data=button)
            for button in buttons
        ]
    )
    # # мой метод
    # for button in buttons:
    #     kb_builder.row(
    #         InlineKeyboardButton(
    #             text=LEXICON.get(button, button),
    #             callback_data=button
    #         )
    #     )

    return kb_builder.as_markup()

# Обединяем похожие вызовы функции создания клваиатуры
# При message.from_user.id и callback.from_user.id - первый параметр
# len(book) - длина книги - это второй параметр
def create_pagination_reply_markup(user_id, book_length):
    return _create_pagination_keyboard(
        'backward',
        f'{users_db[user_id]["page"]}/{book_length}',
        'forward'
    )

