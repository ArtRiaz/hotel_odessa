from aiogram import types, executor
from create_bot import dp, bot
from handlers import start, our_company, back_menu, contact, room, support
from utils.set_command_default import set_commands

async def on_startup(_):
    print("Бот запущен")
    await set_commands(bot=bot)


start.register_handlers_start(dp)
our_company.register_handlers_about(dp)
back_menu.register_handler_back(dp)
contact.register_handler_contact(dp)
room.register_handlers_room(dp)
support.get_support(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
