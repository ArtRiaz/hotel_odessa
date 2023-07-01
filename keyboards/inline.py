from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Наш сайт', url='https://google.com/')
    ], [InlineKeyboardButton('Instagram', url='https://www.instagram.com/artemriazantsev22/')], [
        InlineKeyboardButton('Геолокация', callback_data='Геолокация')
    ], [
        InlineKeyboardButton('Телефон', callback_data='Вызов')
    ]])

    return ikb