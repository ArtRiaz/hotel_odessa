from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_room():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
    ], [InlineKeyboardButton('Детали номера', callback_data='detals')],
        [InlineKeyboardButton('Видеообзор номера', callback_data='promo')],
        [InlineKeyboardButton('Забронировать', callback_data='reserved')],
        [InlineKeyboardButton('Назад в главное меню', callback_data='back')]
    ])

    return ikb


def ikb_detals():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Забронировать', callback_data='reserved')]
    ])

    return ikb
