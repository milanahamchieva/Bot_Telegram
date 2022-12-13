from aiogram.utils.keyboard import InlineKeyboardBuilder


# Keyboards
# def get_kb_cancel() -> InlineKeyboardBuilder:
#     kb_cancel = InlineKeyboardBuilder()
#     kb_cancel.button(
#         text='Отмена',
#         callback_data='cancel'
#     )

#     return kb_cancel.as_markup()


def get_kb_start_img() -> InlineKeyboardBuilder:
    kb_start_img = InlineKeyboardBuilder()
    kb_start_img.button(
        text='Отправить изображение',
        callback_data='start_img_up'
    )
    kb_start_img.button(
        text='Сгенерировать изображение',
        callback_data='start_img_gen'
    )
    kb_start_img.adjust(2)

    return kb_start_img.as_markup()


def get_kb_text_color() -> InlineKeyboardBuilder:
    kb_text_color = InlineKeyboardBuilder()
    kb_text_color.button(
        text='Белый',
        callback_data='txt_color_white'
    )
    kb_text_color.button(
        text='Черный',
        callback_data='txt_color_black'
    )
    kb_text_color.button(
        text='Фиолетовый',
        callback_data='txt_color_violet'
    )
    kb_text_color.button(
        text='Синий',
        callback_data='txt_color_blue'
    )
    kb_text_color.button(
        text='Голубой',
        callback_data='txt_color_indigo'
    )
    kb_text_color.button(
        text='Зеленый',
        callback_data='txt_color_green'
    )
    kb_text_color.button(
        text='Желтый',
        callback_data='txt_color_yellow'
    )
    kb_text_color.button(
        text='Оранжевый',
        callback_data='txt_color_orange'
    )
    kb_text_color.button(
        text='Красный',
        callback_data='txt_color_red'
    )
    kb_text_color.button(
        text='Отмена',
        callback_data='cancel'
    )
    kb_text_color.adjust(3)

    return kb_text_color.as_markup()


def get_kb_img_color() -> InlineKeyboardBuilder:
    kb_img_color = InlineKeyboardBuilder()
    kb_img_color.button(
        text='Белый',
        callback_data='img_color_white'
    )
    kb_img_color.button(
        text='Черный',
        callback_data='img_color_black'
    )
    kb_img_color.button(
        text='Фиолетовый',
        callback_data='img_color_violet'
    )
    kb_img_color.button(
        text='Синий',
        callback_data='img_color_blue'
    )
    kb_img_color.button(
        text='Голубой',
        callback_data='img_color_indigo'
    )
    kb_img_color.button(
        text='Зеленый',
        callback_data='img_color_green'
    )
    kb_img_color.button(
        text='Желтый',
        callback_data='img_color_yellow'
    )
    kb_img_color.button(
        text='Оранжевый',
        callback_data='img_color_orange'
    )
    kb_img_color.button(
        text='Красный',
        callback_data='img_color_red'
    )
    kb_img_color.button(
        text='Отмена',
        callback_data='cancel'
    )
    kb_img_color.adjust(3)

    return kb_img_color.as_markup()


def get_kb_text_position() -> InlineKeyboardBuilder:
    kb_text_position = InlineKeyboardBuilder()
    kb_text_position.button(
        text='Слева',
        callback_data='txt_position_left'
    )
    kb_text_position.button(
        text='По центру',
        callback_data='txt_position_centr'
    )
    kb_text_position.button(
        text='Справа',
        callback_data='txt_position_right'
    )
    kb_text_position.button(
        text='Отмена',
        callback_data='cancel'
    )
    kb_text_position.adjust(3)

    return kb_text_position.as_markup()
