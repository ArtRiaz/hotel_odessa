from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Условия бронирования')
    ], [
        KeyboardButton('Позвонить нам')
    ], [
        KeyboardButton('Задать вопрос')
    ], [
        KeyboardButton('Назад в главное меню')
    ]

    ])

    return kb


def get_data():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('Заполнить свои данные')],
        [KeyboardButton('Назад в главное меню')],
        [KeyboardButton('Инструкция для админа.ОБЯЗАТЕЛЬНО ПРОЧИТАТЬ')]
    ])

    return kb
