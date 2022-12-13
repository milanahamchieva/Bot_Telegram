from PIL import Image, ImageDraw, ImageFont
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile


async def send_gen_img(message: types.Message, bot: Bot):
    await message.answer('Изображение с Вашими параметрами готово')
    gen_img = FSInputFile('img.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=gen_img)

async def gen_final_img(message: types.Message, state: FSMContext, bot: Bot):
    font = ImageFont.truetype('fonts\Roboto-Regular.ttf', size=25)
    img_data = await state.get_data()
    img_mode = img_data.get('img')
    text = img_data.get('text')
    text_position = img_data.get('txt_position')
    text_color = img_data.get('text_color')
    
    if img_mode == 0:
        img_height = int(img_data.get('img_height'))
        img_width = int(img_data.get('img_width'))
        img_color = img_data.get('img_color')
        W, H = (img_width,img_height)
        img = Image.new('RGB', (W, H), img_color)
        draw_text = ImageDraw.Draw(img)
        w, h = draw_text.textsize(text)
        if text_position == 'left':
            draw_text.text((((W-w)/8,(H-h)/2)), text, font=font, fill=text_color)
        elif text_position == 'centr':
            draw_text.text((((W-w)/2,(H-h)/2)), text, font=font, fill=text_color)        
        elif text_position == 'right':
            draw_text.text(((W-((W-w)/4),(H-h)/2)), text, font=font, fill=text_color)
        img.save('img.jpg')
        await send_gen_img(message, bot)
        print_data = f'Параметры генерации\r\n' \
            f'Вид операции: Сгенерировать изображение\n' \
            f'Цвет изображения: {img_color}\n' \
            f'Высота изображения: {img_height}\n' \
            f'Ширина изображения: {img_width}\n' \
            f'Текст: {text}\n' \
            f'Цвет текста: {text_color}\n' \
            f'Местоположение текста: {text_position}' 
        await send_gen_img(message, bot)     
    elif img_mode == 1:
        img = Image.open('img.jpg')
        draw_text = ImageDraw.Draw(img)
        W, H = img.size
        w, h = draw_text.textsize(text)
        if text_position == 'left':
            draw_text.text((((W-w)/8,(H-h)/2)), text, font=font, fill=text_color)
        elif text_position == 'centr':
            draw_text.text((((W-w)/2,(H-h)/2)), text, font=font, fill=text_color)        
        elif text_position == 'right':
            draw_text.text(((W-((W-w)/4),(H-h)/2)), text, font=font, fill=text_color)
        img.save('img.jpg')
        print_data = f'Параметры генерации\r\n' \
            f'Вид операции: На готовом изображении\n' \
            f'Текст: {text}\n' \
            f'Цвет текста: {text_color}\n' \
            f'Местоположение текста: {text_position}'    
        await send_gen_img(message, bot)      
    await message.answer(print_data)
    await state.clear()
