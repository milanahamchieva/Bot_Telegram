import utilite
import generation
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext


async def call_txt_color(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'txt_color_white':
        await state.update_data(text_color='#ffffff')
    elif call.data == 'txt_color_black':
        await state.update_data(text_color='#000000')
    elif call.data == 'txt_color_violet':
        await state.update_data(text_color='#ee82ee')
    elif call.data == 'txt_color_blue':
        await state.update_data(text_color='#0000ff')
    elif call.data == 'txt_color_indigo':
        await state.update_data(text_color='#4b0082')
    elif call.data == 'txt_color_green':
        await state.update_data(text_color='#008000')
    elif call.data == 'txt_color_yellow':
        await state.update_data(text_color='#ffff00')
    elif call.data == 'txt_color_orange':
        await state.update_data(text_color='#ffa500')
    elif call.data == 'txt_color_red':
        await state.update_data(text_color='#ff0000')
    else:
        return
    await utilite.get_text_position(call.message, state)
    await call.answer()

async def call_txt_position(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    if call.data == 'txt_position_left':
        await state.update_data(txt_position='left')
    elif call.data == 'txt_position_centr':
        await state.update_data(txt_position='centr')
    elif call.data == 'txt_position_right':
        await state.update_data(txt_position='right')
    else:
        return
    await generation.gen_final_img(call.message, state, bot)
    await call.answer()

async def call_img_color(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'img_color_white':
        await state.update_data(img_color='#ffffff')
    elif call.data == 'img_color_black':
        await state.update_data(img_color='#000000')
    elif call.data == 'img_color_violet':
        await state.update_data(img_color='#ee82ee')
    elif call.data == 'img_color_blue':
        await state.update_data(img_color='#0000ff')
    elif call.data == 'img_color_indigo':
        await state.update_data(img_color='#4b0082')
    elif call.data == 'img_color_green':
        await state.update_data(img_color='#008000')
    elif call.data == 'img_color_yellow':
        await state.update_data(img_color='#ffff00')
    elif call.data == 'img_color_orange':
        await state.update_data(img_color='#ffa500')
    elif call.data == 'img_color_red':
        await state.update_data(img_color='#ff0000')
    else:
        return
    await utilite.get_img_size(call.message, state)
    await call.answer()

async def call_cancel(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Задача сброшена, начните сначала')
    await state.clear()
    await utilite.send_welcome(call.message)
    await call.answer()

async def call_start(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'start_img_up':
        await utilite.get_img(call.message)
    elif call.data == 'start_img_gen':
        await utilite.get_img_color(call.message, state)
    else:
        return
    await call.answer()
