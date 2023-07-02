from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards.reply import kb_menu, get_kb_menu, get_back


async def cmd_start(message: types.Message):
    with open('../media/glavhaya.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption=f'<b> Добро пожаловать, {message.from_user.full_name}!\n </b>'
                                     f'Если вы еще не ощущали настоящий изыск, то это тот самый случай когда можно окунуться '
                                     f'в отличное приключение '
                                     f'в Одессе на поборежье Черного моря'
                                     f'в самом чудесном отеле Sfumato'
                             , reply_markup=kb_menu())


async def cmd_menu(message: types.Message):
    await message.answer('Управления меню', reply_markup=get_kb_menu())


## Инструкция

async def istruct(message: types.Message):
    await message.answer(f'Приветствую, уважаемый {message.from_user.first_name}!\n'
                         f'Это короткая инструкция к призентационому боту, он на данный момент не является\n'
                         f'готовым продуктом, и носит ознакомительный характер.\n  '
                         f'Когда вы запускаете бота вы видете основную кнопку меню,\n'
                         f'а также синюю кнопку меню для запуска или перезапуска бота\n '
                         f'также в это меню мы можем добавить любую команду для бота или функцию.\n'
                         f'В основном меню 3 раздела "Про нас","Номера","Контакты".\n'
                         f'В разделе про нас мы можем описать любой ваш контент и вставить любые фотки и видео\n'
                         f'В разделе "контакты" мы можем описать как с Вами связаться и т.д.\n'
                         f'В разделе "Номера" описание ваших номеров и бронирование, также можно задать вопрос\n'
                         f'или связаться со стойкой регистрации\n'
                         f'При бронировании клиент должен заполнить свои данные\n'
                         f' написать дату заезда и выезда в таком формате: 22.07.2023\n'
                         f'а также имя и фамилию, контактные данные\n, после бронирования и оплаты \n'
                         f'вам будет приходить уведомление и вся информация о бронировании.\n'
                         f'На данный момент установленна тестовая оплата, вы можете посмотреть как это работает,\n'
                         f'выбрать способ оплаты карта и ввести реквизиты: номер карты:4242424242424242 06/24 cvv 123\n'
                         f'Для полной версии бота предлагаю подключить базу данных, создать панель администратара\n'
                         f'для управления ботов, рассылкой своей рекламы, введение статистики и многих других функций\n'
                         f'Телеграм бот верный помошник в вашем бизнесе! Жду от Вас информации и до связи !',
                         reply_markup=get_kb_menu())


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_menu, Text(equals='Меню'))
    dp.register_message_handler(istruct, Text(equals='Инструкция для админа.ОБЯЗАТЕЛЬНО ПРОЧИТАТЬ'))
