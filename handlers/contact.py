from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from keyboards.inline import ikb_contact
from keyboards.reply import get_back
from aiogram.types import CallbackQuery


async def cmd_contact(message: types.Message):
    await message.answer("Как с нами связаться:", reply_markup=get_back())
    await message.delete()
    await message.answer('Выберете соц сеть или позвоните нам:', reply_markup=ikb_contact())


async def send_geo(callback: CallbackQuery):
    await callback.message.delete()
    await callback.bot.send_location(chat_id=callback.from_user.id,
                                     latitude=46.4804680,
                                     longitude=30.7432531,
                                     reply_markup=get_back()
                                     )


async def send_phone(callback: CallbackQuery):
    await callback.message.delete()
    await callback.bot.send_contact(chat_id=callback.from_user.id,
                                    phone_number='+38(093)5286359',
                                    first_name='Стойка регистрации',
                                    reply_markup=get_back())


def register_handler_contact(dp: Dispatcher):
    dp.register_message_handler(cmd_contact, Text(equals='Контакты'))
    dp.register_callback_query_handler(send_geo, text='Геолокация')
    dp.register_callback_query_handler(send_phone, text='Вызов')
