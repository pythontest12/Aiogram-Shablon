from aiogram import types
from googletrans import Translator
from loader import dp

tarjimon = Translator()
# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):
    til = tarjimon.detect(text=message.text).lang
    if til == 'uz':
        tarjima_qilish_en = tarjimon.translate(text=message.text,dest='en',src='uz').text
        await message.answer(tarjima_qilish_en)
