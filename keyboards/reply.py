from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Меню')
    ]])

    return kb


def get_kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Про нас')
    ], [
        KeyboardButton('Номера')
    ], [
        KeyboardButton('Контакты')
    ]

    ])

    return kb


def get_back():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Назад в главное меню')
    ]])

    return kb