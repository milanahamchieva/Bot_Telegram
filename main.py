import config
import callbacks
import utilite
import asyncio
import logging
from aiogram import F
from aiogram.fsm.context import FSMContext
from utilite import GenOption
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import BotCommand


async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.DEBUG)

    # bot_commands = (
    # ("start", "Начало работы с ботом", "Запускается весь алгоритм с самого начала"),
    # ("help", "Помощь и справка", "Описание работы бота")
    # )

    # commands_for_bot = []
    # for cmd in bot_commands:
    #     commands_for_bot.append(BotCommand(command=cmd[0], description=[1]))

    # Объект бота
    bot = Bot(token=config.TOKEN, parse_mode="HTML")
    # Диспетчер
    dp = Dispatcher()
    # await bot.set_my_commands(commands=commands_for_bot)

    # dp.message.register(utilite.start_bot)
    dp.message.register(utilite.get_photo, F.photo)
    dp.message.register(utilite.get_text, GenOption.waitin_text)
    dp.message.register(utilite.get_img_height, GenOption.waitin_img_height)
    dp.message.register(utilite.get_img_width, GenOption.waitin_img_width)
    dp.message.register(utilite.send_welcome, Command(commands=['start']))
    #CallBacks:
    dp.callback_query.register(callbacks.call_start, F.data.startswith('start_img_'))
    dp.callback_query.register(callbacks.call_cancel, F.data == 'cancel')
    dp.callback_query.register(callbacks.call_txt_color, F.data.startswith('txt_color_'))
    dp.callback_query.register(callbacks.call_txt_position, F.data.startswith('txt_position_'))
    dp.callback_query.register(callbacks.call_img_color, F.data.startswith('img_color_'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
