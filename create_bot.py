from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN_API = '6244815623:AAHViMFB6OlqiCCVypAOCuluK-hHA2IT7Ns'
#PAYMENT_TOKEN = '632593626:TEST:sandbox_i43329160256'
storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)

support_ids = [
    1064938479
]