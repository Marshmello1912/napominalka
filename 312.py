from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
bot = Bot(token='5423662964:AAEJgM43juo13UHfZzOaPkMP1ngn90svM7k')
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    send_message = await bot.send_message(chat_id= message.chat.id, text = '@NikitaShmelev9983 Оно тебя любит♥')
executor.start_polling(dp)