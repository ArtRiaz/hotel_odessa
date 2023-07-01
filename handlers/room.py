from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards.reply import kb_menu, get_kb_menu, get_back
from keyboards.inline_room import ikb_room, ikb_detals
from keyboards.reply_room import get_kb_menu
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.reply_room import get_data
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
import calendar



async def panorama_room(message: types.Message):
    with open('/Users/artem/Desktop/hotel_panorama.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption=f'Если вы {message.from_user.first_name} еще не ощущали настоящий изыск, то это '
                                     f'тот самый случай когда можно окунуться в отличное приключение в Одессе на '
                                     f'поборежье Черного моря '

                             , reply_markup=ikb_room())


async def panorama_detale(call: CallbackQuery):
    with open('/Users/artem/Desktop/panorama1.jpg', 'rb') as photo1:
        await call.bot.send_photo(chat_id=call.from_user.id,
                                  photo=photo1,
                                  caption=f'<b>Концепция номера H2</b>'
                                          f'Спрятанный в самом сердце южного берега в Одессе и всего в 10 минутах от '
                                          f'знаковых достопримечательностей города и оживленного района Аркадия, '
                                          f'Sfumato является одним из лучших роскошных отелей в южной столице. Спрятанный в '
                                          f'самом сердце южного берега в Одессе и всего в 10 минутах от знаковых '
                                          f'достопримечательностей города и оживленного района Аркадия, Sfumato является одним '
                                          f'из лучших роскошных отелей в южной столице. ', reply_markup=get_kb_menu()
                                  )

    with open('/Users/artem/Desktop/panorama2.jpg', 'rb') as photo2:
        await call.bot.send_photo(chat_id=call.from_user.id,
                                  photo=photo2,
                                  caption=
                                  f'<b>Планировка номера</b>'
                                  f'Спрятанный в самом сердце южного берега в Одессе и всего в 10 минутах от знаковых '
                                  f'достопримечательностей города и оживленного района Аркадия, Sfumato является одним '
                                  f'из лучших роскошных отелей в южной столице.')

    with open('/Users/artem/Desktop/panorama3.jpg', 'rb') as photo3:
        await call.bot.send_photo(chat_id=call.from_user.id,
                                  photo=photo3,
                                  caption=
                                  f'Спрятанный в самом сердце южного берега в Одессе и всего в 10 минутах от знаковых '
                                  f'достопримечательностей города и оживленного района Аркадия, Sfumato является одним '
                                  f'из лучших роскошных отелей в южной столице.', reply_markup=ikb_detals())


class RoomOrder(StatesGroup):
    check_in = State()
    departe = State()
    full_name = State()
    email = State()


async def order(call: CallbackQuery):
    await call.message.answer('Для бронирования номера заполните данные', reply_markup=get_data())


async def order_start(message: types.Message):
    await RoomOrder.check_in.set()
    await message.answer(f'Для бронирование номера введите дату заезда: ')


async def check_in(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["check_in"] = message.text
    await RoomOrder.next()
    await message.reply("Введите дату отьезда: ")


async def departe(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["departe"] = message.text
    await RoomOrder.next()
    await message.answer("Введите свое имя и фамилию: ")


async def full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["full_name"] = message.text
    await RoomOrder.next()
    await message.answer("Введите свой контактный e-mail: ")


async def get_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["email"] = message.text
        print(data)

        data = await state.get_data()
        check_in = data.get('check_in')
        departe = data.get('departe')
        full_name = data.get('full_name')
    await message.answer(f'Ваша регистрация успешно выполнена.\n'
                         f'Ваша дата заезда: {check_in}\n'
                         f'Ваша дата выезда: {departe}\n'
                         f'Ваше Имя и Фамилия: {full_name}', reply_markup=get_back()
                         )

    await state.finish()
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Номер люкс с панорамным окном',
        description='Люкс',
        payload='Не видно пользователю , можно использовать для сбора статистики',
        provider_token='1877036958:TEST:43ea5330d3b1456d983819486288604d3d540a38',
        currency='UAH',
        prices=[
            LabeledPrice(
                label='Номер Люкс',
                amount=120000
            )],
        need_phone_number=True,
        need_email=True)


async def checkout_procces(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def s_pay(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Оплата прошла удачно!', reply_markup=get_kb_menu())


async def rules_reserved(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f"<b>Условия сотрудничества</b>\n"
                                                              f"<b>Пожалуйста, внимательно ознакомьтесь с условиями бронирования и оплаты!</b>\n"
                                                              f"Чтобы забронировать комнату в ОТЕЛЕ «Sfumato», воспользуйтесь любым удобным для Вас способом: \n"
                                                              f"01.По телефону\n"
                                                              f"Наши контакты в одессе: 093 528 62 59\n"
                                                              f"02.Через сервисы бронирования\n"
                                                              f"Booking:  https://www.booking.com/hotel/au/SfumatoOdessa\n"
                                                              f"Bnovo:\n"
                                                              f"https://www.bnovo.com/SfumatoOdessa\n"
                                                              f"03.На нашем сайте\n"
                                                              f"По телефону, конечно же вот эти телефоны: 093 528 63 59, или в разделе контакты\n"
                                                              f"Через форму контактов \n"
                                                              f"перейдите в контакты чтобы отправить нам сообщение\n"
                                                              f"Умови проживання\n"
                                                              f"Заїзд після 14:00. Виїзд до 12:00.\n"
                                                              f"В стоимость входит завтрак.\n",
                           reply_markup=get_kb_menu())


async def send_phone(message: types.Message):
    await message.delete()
    await bot.send_contact(chat_id=message.from_user.id,
                           phone_number='+38(093)5286359',
                           first_name='Стойка регистрации',
                           reply_markup=get_back())


def register_handlers_room(dp: Dispatcher):
    dp.register_message_handler(panorama_room, Text(equals='Номера'))
    dp.register_message_handler(rules_reserved, Text(equals='Условия бронирования'))
    dp.register_callback_query_handler(panorama_detale, text='detals')
    dp.register_callback_query_handler(order, text='reserved')
    dp.register_message_handler(order_start, Text(equals='Заполнить свои данные'), state=None)
    dp.register_message_handler(check_in, state=RoomOrder.check_in)
    dp.register_message_handler(departe, state=RoomOrder.departe)
    dp.register_message_handler(full_name, state=RoomOrder.full_name)
    dp.register_message_handler(get_phone, state=RoomOrder.email)
    dp.register_message_handler(send_phone, Text(equals='Позвонить нам'))
    dp.register_pre_checkout_query_handler(checkout_procces, lambda q: True)
    dp.register_message_handler(s_pay, content_types=ContentType.SUCCESSFUL_PAYMENT)
