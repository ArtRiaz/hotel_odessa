from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.reply import kb_menu, get_kb_menu, get_back
from aiogram.dispatcher.filters import Text
import asyncio

photo1 = open('/Users/artem/Desktop/hotel_about1.jpg', 'rb')
photo2 = open('/Users/artem/Desktop/hotel_about2.jpg', 'rb')


async def cmd_menu(message: types.Message):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo1,
                             caption=f'<b>Спрятанный в самом сердце южного берега в Одессе и всего в 10 минутах от '
                                     f'знаковых достопримечательностей города и оживленного района Аркадия, '
                                     f'Sfumato является одним из лучших роскошных отелей в южной столице.</b>',
                             reply_markup=get_back())
        await asyncio.sleep(1)

        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo2,
                             caption=f'<b>Спрятанный в самом сердце южного берега в Одессе и всего в 10 минутах от '
                                     f'знаковых достопримечательностей города и оживленного района Аркадия, '
                                     f'Sfumato является одним из лучших роскошных отелей в южной столице.</b>',
                             reply_markup=get_back())


def register_handlers_about(dp: Dispatcher):
    dp.register_message_handler(cmd_menu, Text(equals='Про нас'))
