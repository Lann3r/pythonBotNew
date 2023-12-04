from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='❤️Новые папины дочки', callback_data='new_daughter')
    keyboard_builder.button(text='❤️Дочки знают', callback_data='know_daughter')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def new_daughter_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='1 серия', callback_data='1new')
    keyboard_builder.button(text='2 серия', callback_data='2new')
    keyboard_builder.button(text='3 серия', callback_data='3new')
    keyboard_builder.button(text='4 серия', callback_data='4new')
    keyboard_builder.button(text='5 серия', callback_data='5new')
    keyboard_builder.button(text='6 серия', callback_data='6new')
    keyboard_builder.button(text='7 серия', callback_data='7new')
    keyboard_builder.button(text='8 серия', callback_data='8new')
    keyboard_builder.button(text='9 серия', callback_data='9new')
    keyboard_builder.button(text='10 серия', callback_data='10new')
    keyboard_builder.button(text='11 серия', callback_data='11new')
    keyboard_builder.button(text='12 серия', callback_data='12new')
    keyboard_builder.button(text='13 серия', callback_data='13new')
    keyboard_builder.button(text='14 серия', callback_data='14new')
    keyboard_builder.button(text='15 серия', callback_data='15new')
    keyboard_builder.button(text='16 серия', callback_data='16new')
    keyboard_builder.button(text='17 серия', callback_data='17new')
    keyboard_builder.button(text='18 серия', callback_data='18new')
    keyboard_builder.button(text='19 серия', callback_data='19new')
    keyboard_builder.button(text='20 серия', callback_data='20new')
    keyboard_builder.button(text='Выбрать другой сериал↩️', callback_data='another')

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()


def know_daughter_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='1 серия', callback_data='1know')
    keyboard_builder.button(text='2 серия', callback_data='2know')
    keyboard_builder.button(text='3 серия', callback_data='3know')
    keyboard_builder.button(text='4 серия', callback_data='4know')
    keyboard_builder.button(text='5 серия', callback_data='5know')
    keyboard_builder.button(text='6 серия', callback_data='6know')
    keyboard_builder.button(text='7 серия', callback_data='7know')
    keyboard_builder.button(text='8 серия', callback_data='8know')
    keyboard_builder.button(text='9 серия', callback_data='9know')
    keyboard_builder.button(text='10 серия', callback_data='10know')
    keyboard_builder.button(text='11 серия', callback_data='11know')
    keyboard_builder.button(text='12 серия', callback_data='12know')
    keyboard_builder.button(text='13 серия', callback_data='13know')
    keyboard_builder.button(text='14 серия', callback_data='14know')
    keyboard_builder.button(text='15 серия', callback_data='15know')
    keyboard_builder.button(text='16 серия', callback_data='16know')
    keyboard_builder.button(text='17 серия', callback_data='17know')
    keyboard_builder.button(text='18 серия', callback_data='18know')
    keyboard_builder.button(text='19 серия', callback_data='19know')
    keyboard_builder.button(text='20 серия', callback_data='20know')
    keyboard_builder.button(text='Выбрать другой сериал↩️', callback_data='another')

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()


def select_another_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Выбрать другую серию↩️', callback_data='select')
    return keyboard_builder.as_markup()


def select_another_keyboard_know():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Выбрать другую серию↩️', callback_data='select_know')
    return keyboard_builder.as_markup()


def check_sub_button():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Проверить подписку!✅', callback_data='check')
    return keyboard_builder.as_markup()
