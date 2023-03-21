from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# from PIL import Image
FlowersNames  = ["d:\OrionLoop\AST-BL-01_02.jpg",
                "d:\OrionLoop\AST-BU-01_01.jpg",
                "d:\OrionLoop\AST-BU-02_01.jpg" ]

# img1 = Image.open(FlowersNames[0],'rb' )
# print(img1)
# img2 = Image.open(FlowersNames[1],'rb')
# img3 = Image.open(FlowersNames[2],'rb')

# from config import TOKEN


bot = Bot(token='6118253667:AAE7x6OQThgJKM0VUq4I8ov6tGnd2ivcHUA')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
#    await message.reply("Привет!\nНапиши мне что-нибудь!")
    await message.answer("Привет!\nНапиши мне что-нибудь!")



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
#    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
    await message.answer("Вас приветствует ТБ OrionLoop")
    await message.answer("/help - это сообщение")
    await message.answer("/1 - Выбор таблицы 1")
    await message.answer("/2 - Выбор таблицы 1")
    await message.answer("/3 - Выбор таблицы 1 \n  и вот это ")
    await message.answer("/4 - Выбор таблицы 1")
    await message.answer("/send  -  отправкка")


@dp.message_handler(commands=['send'])
async def process_help_command(message: types.Message):
    await message.reply("Введите имя  чегото")



@dp.message_handler(commands=['1'])
async def process_help_command(message: types.Message):
#    await message.reply("здесь будет картинка")
    await bot.send_photo(chat_id=message.from_user.id,photo= img1)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    # await message.answer("Привет Лошара")



if __name__ == '__main__':
    executor.start_polling(dp)



#
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
#
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token="12345678:AaBbCcDdEeFfGgHh")
# # Диспетчер
# dp = Dispatcher(bot)
#
# # Хэндлер на команду /start
# @dp.message(commands=["start"])
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
#
# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())