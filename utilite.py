from aiogram.types import Message
from aiogram import Bot
import keyboards
import commands
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class GenOption(StatesGroup):
    waitin_img = State()
    waitin_img_height = State()
    waitin_img_width = State()
    waitin_img_color = State()
    waitin_text = State()
    # waitin_text_fonts = State()
    waitin_text_color = State()
    waitin_text_position = State()

async def start_bot(message: Message, bot: Bot):
    await commands.set_commands(bot)
    await bot.send_message(text='Бот запущен')

async def get_img(message: types.Message):
    await message.answer('Пришлите боту фото для обработки')

async def get_photo(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(img=1)
    img = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(img.file_path, 'img.jpg')
    await message.answer(text='Отлично! Теперь введите текс для картинки')
    await state.set_state(GenOption.waitin_text)

async def get_text(message: Message, state: FSMContext):
    await message.answer(
        text='Теперь выберите цвет текста',
        reply_markup=keyboards.get_kb_text_color()
        )
    await state.update_data(text=message.text)
    await state.set_state(GenOption.waitin_text_color)

async def get_text_color(message: types.Message, state: FSMContext):
    await message.answer(
        text='Теперь выберите цвет текста. Нажмите соответствующую кнопку на клавиатуре',
        reply_markup=keyboards.get_kb_text_color()
        )
    await state.set_state(GenOption.waitin_text_position)

async def get_text_position(message: types.Message, state: FSMContext):
    await message.answer(
        text='На этом шаге определим местоположение текста',
        reply_markup=keyboards.get_kb_text_position()
        )
    await state.set_state(GenOption.waitin_text_position)

async def get_img_color(message: types.Message, state: FSMContext):
    await message.answer(
        text='Задайте параметры изображение(Цвет). Выберите соответствующую кнопку на клавиатуре',
        reply_markup=keyboards.get_kb_img_color()
        )
    await state.update_data(img=0)
    await state.set_state(GenOption.waitin_img_color)

async def get_img_size(message: types.Message, state: FSMContext):
    await message.answer('Задайте параметры изображение(Высота). Введите значение в пикселях, только цифры')
    await state.set_state(GenOption.waitin_img_height)

async def get_img_height(message: types.Message, state: FSMContext):
    await state.update_data(img_height=message.text)
    await message.answer('Задайте параметры изображение(Ширина). Введите значение в пикселях, только цифры')
    await state.set_state(GenOption.waitin_img_width)

async def get_img_width(message: types.Message, state: FSMContext):
    await state.update_data(img_width=message.text)
    await message.answer(text='Отлично! Теперь введите текс для картинки')
    await state.set_state(GenOption.waitin_text)

async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(
        text='Привет!\nЯ - КартинкаБот!\nЯ накладываю текст на изображение. Отправь мне изображение или я сгенерирую его сам, затем пришли мне текст и я наложу его на изображение. Приступим?', 
        reply_markup=keyboards.get_kb_start_img()
        )
    await state.set_state(GenOption.waitin_img)