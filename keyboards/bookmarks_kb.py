from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON
from services.file_handling import book

"""Клавиатура для работы с закладками"""

def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(text=f'{button} - {book[button][:100]}',
                                 callback_data=str(button)
                                 )
        )
    # Добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(
        InlineKeyboardButton(text=LEXICON.get('edit_bookmarks_button', 'УПС!'),
                             callback_data='edit_bookmarks'),
        InlineKeyboardButton(text=LEXICON.get('cancel', 'УПС!'),
                             callback_data='cancel'),
        width=2
    )

    return kb_builder.as_markup()

def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for button in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f"{LEXICON.get('del', 'УПС')} {button} - {book[button][:100]}",
                callback_data=f'{button}del'
            )
        )
        # Добавляем в конец клавиатуры кнопку "Отменить"
        kb_builder.row(
            InlineKeyboardButton(
                text=LEXICON.get('cancel', 'УПС'),
                callback_data='cancel'
            )
        )
        return kb_builder.as_markup()
