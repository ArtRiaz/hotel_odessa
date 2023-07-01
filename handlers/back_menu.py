from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from handlers.start import get_kb_menu
from aiogram.types import CallbackQuery

async def cmd_back(message: types.Message):
    await message.delete()
    await message.answer('Вы вернулись в главное меню',
                         reply_markup=get_kb_menu())


async def cmd_back_query(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('Вы вернулись в главное меню',
                         reply_markup=get_kb_menu())

def register_handler_back(dp: Dispatcher):
    dp.register_message_handler(cmd_back, Text(equals='Назад в главное меню'))
    dp.register_callback_query_handler(cmd_back_query, text='back')
