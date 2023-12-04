from aiogram import types, Dispatcher
from aiogram.types import Message
from сore.Keyboards.inline import get_inline_keyboard, new_daughter_keyboard, know_daughter_keyboard, \
    select_another_keyboard, check_sub_button, select_another_keyboard_know

dp = Dispatcher()


async def get_inline(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=get_inline_keyboard())


async def get_start(message: Message):
    await message.answer(
        'Добро пожаловать!❤️Чтобы посмотреть серии вы должны\nподписаться☑️ на наш канал \
с милыми котиками🐈\n https://t.me/+DNONd2h01Ic2OTIy',
        reply_markup=check_sub_button())


async def callback_series(callback: types.CallbackQuery):
    code = callback.data
    if code == 'new_daughter':
        await callback.message.edit_text("Сериал: Новые папины дочки. Выберите серию:",
                                         reply_markup=new_daughter_keyboard())

    elif code == 'know_daughter':
        await callback.message.edit_text("Сериал: Дочки знают. Выберите серию:",
                                         reply_markup=know_daughter_keyboard())

    # Выбор других серии
    if code == 'select':
        await callback.message.edit_text("Сериал: Новые папины дочки. Выберите серию:",
                                         reply_markup=new_daughter_keyboard())

    if code == 'select_know':
        await callback.message.edit_text("Сериал: Новые папины дочки. Выберите серию:",
                                         reply_markup=know_daughter_keyboard())

    elif code == 'another':
        await callback.message.edit_text('Пожалуйста, выберите сериал:', reply_markup=get_inline_keyboard())

    elif code == 'check':
        await callback.message.answer('Добро пожаловать! Выберите сериал:', reply_markup=get_inline_keyboard())

    # Новые папины дочки серии
    elif code == '1new':
        await callback.message.edit_text("Новые папины дочки 1 серия: \n https://cloud.mail.ru/public/thj7/iJQgJqryJ ",
                                         reply_markup=select_another_keyboard())

    elif code == '2new':
        await callback.message.edit_text("Новые папины дочки 2 серия: \n https://cloud.mail.ru/public/Dym7/xjZ6NG9LW ",
                                         reply_markup=select_another_keyboard())

    elif code == '3new':
        await callback.message.edit_text("Новые папины дочки 3 серия: \n https://cloud.mail.ru/public/7o2o/z9Rvx8QpS ",
                                         reply_markup=select_another_keyboard())

    elif code == '4new':
        await callback.message.edit_text("Новые папины дочки 4 серия: \n https://cloud.mail.ru/public/zwrD/sF8r9xfCH ",
                                         reply_markup=select_another_keyboard())

    elif code == '5new':
        await callback.message.edit_text("Новые папины дочки 5 серия: \n https://cloud.mail.ru/public/mvu7/cTpLYtEJh ",
                                         reply_markup=select_another_keyboard())

    elif code == '6new':
        await callback.message.edit_text("Новые папины дочки 6 серия: \n https://cloud.mail.ru/public/Yutv/BKCkhD9S9 ",
                                         reply_markup=select_another_keyboard())

    elif code == '7new':
        await callback.message.edit_text("Новые папины дочки 7 серия: \n https://cloud.mail.ru/public/KRDu/D8bn2brEM ",
                                         reply_markup=select_another_keyboard())

    elif code == '8new':
        await callback.message.edit_text("Новые папины дочки 8 серия: \n https://cloud.mail.ru/public/VuP8/YvdkPDEtY ",
                                         reply_markup=select_another_keyboard())

    elif code == '9new':
        await callback.message.edit_text("Новые папины дочки 9 серия: \n https://cloud.mail.ru/public/fS47/2H8BsKoh1 ",
                                         reply_markup=select_another_keyboard())

    elif code == '10new':
        await callback.message.edit_text("Новые папины дочки 10 серия: \n https://cloud.mail.ru/public/XQ8v/DDFqi8kR1 ",
                                         reply_markup=select_another_keyboard())

    elif code == '11new':
        await callback.message.edit_text("Новые папины дочки 11 серия: \n https://cloud.mail.ru/public/2rEV/3UcTBKSJo ",
                                         reply_markup=select_another_keyboard())

    elif code == '12new':
        await callback.message.edit_text("Новые папины дочки 12 серия: \n https://cloud.mail.ru/public/51BC/1VU9jdPcT ",

                                         reply_markup=select_another_keyboard())
    elif code == '13new':
        await callback.message.edit_text("Новые папины дочки 13 серия: \n https://cloud.mail.ru/public/7Y3E/WWDnc69Zm ",

                                         reply_markup=select_another_keyboard())
    elif code == '14new':
        await callback.message.edit_text("Новые папины дочки 14 серия: \n https://cloud.mail.ru/public/76cH/SXmzmgtrr ",

                                         reply_markup=select_another_keyboard())
    elif code == '15new':
        await callback.message.edit_text("Новые папины дочки 15 серия: \n https://cloud.mail.ru/public/vhqN/X8r1wd6rZ ",

                                         reply_markup=select_another_keyboard())
    elif code == '16new':
        await callback.message.edit_text("Новые папины дочки 16 серия: \n https://cloud.mail.ru/public/9YWr/SCMD6X69c ",

                                         reply_markup=select_another_keyboard())
    elif code == '17new':
        await callback.message.edit_text("Новые папины дочки 17 серия: \n https://cloud.mail.ru/public/aBEf/Y5MLca6dm ",

                                         reply_markup=select_another_keyboard())
    elif code == '18new':
        await callback.message.edit_text("Новые папины дочки 18 серия: \n https://cloud.mail.ru/public/E7Tq/EZg7FXFQH ",

                                         reply_markup=select_another_keyboard())
    elif code == '19new':
        await callback.message.edit_text("Новые папины дочки 19 серия: \n https://cloud.mail.ru/public/UGP2/dxGoqqpYm ",

                                         reply_markup=select_another_keyboard())
    elif code == '20new':
        await callback.message.edit_text("Новые папины дочки 20 серия: \n https://cloud.mail.ru/public/esix/7CZnEKqmx ",
                                         reply_markup=select_another_keyboard())

# Дочки знают
    elif code == '1know':
        await callback.message.edit_text("Дочки знают 1 серия👇: \n https://cloud.mail.ru/public/t7SW/dUBnLMzjo ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '2know':
        await callback.message.edit_text("Дочки знают 2 серия👇: \n https://cloud.mail.ru/public/rbq9/VeAj2UP6e ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '3know':
        await callback.message.edit_text("Дочки знают 3 серия👇: \n https://cloud.mail.ru/public/DU31/scAPn2nq7 ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '4know':
        await callback.message.edit_text("Дочки знают 4 серия👇: \n https://cloud.mail.ru/public/9jXA/ZrTmEZ592 ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '5know':
        await callback.message.edit_text("Дочки знают 5 серия👇: \n https://cloud.mail.ru/public/Gcqe/KxcsDCCym ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '6know':
        await callback.message.edit_text("Дочки знают 6 серия👇: \n https://cloud.mail.ru/public/yMnB/o75XEsg44 ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '7know':
        await callback.message.edit_text("Дочки знают 7 серия👇: \n https://cloud.mail.ru/public/ii2V/yMm6695cX ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '8know':
        await callback.message.edit_text("Дочки знают 8 серия👇: \n https://cloud.mail.ru/public/DmGb/vJDL89G9G ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '9know':
        await callback.message.edit_text("Дочки знают 9 серия👇: \n https://cloud.mail.ru/public/RNCM/K6eKhwuHN ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '11know':
        await callback.message.edit_text("Дочки знают 11 серия👇: \n https://cloud.mail.ru/public/dUw4/8XTQCSbzT ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '12know':
        await callback.message.edit_text("Дочки знают 12 серия👇: \n https://cloud.mail.ru/public/euDz/c6LJSEZen ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '13know':
        await callback.message.edit_text("Дочки знают 13 серия👇: \n https://cloud.mail.ru/public/UpK6/pLuTccK6s ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '14know':
        await callback.message.edit_text("Дочки знают 14 серия👇: \n https://cloud.mail.ru/public/yzKp/Bm9XHYyhb ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '15know':
        await callback.message.edit_text("Дочки знают 15 серия👇: \n https://cloud.mail.ru/public/kE38/9E5oPEgL3 ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '16know':
        await callback.message.edit_text("Дочки знают 16 серия👇: \n https://cloud.mail.ru/public/j8Sc/zapicMPce ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '17know':
        await callback.message.edit_text("Дочки знают 17 серия👇: \n https://cloud.mail.ru/public/PhRB/iBsB5LrZd ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '18know':
        await callback.message.edit_text("Дочки знают 18 серия👇: \n https://cloud.mail.ru/public/wWnq/eoDP7WLfc ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '19know':
        await callback.message.edit_text("Дочки знают 19 серия👇: \n https://cloud.mail.ru/public/o4Mc/akAkDtNoX ",
                                         reply_markup=select_another_keyboard_know())

    elif code == '20know':
        await callback.message.edit_text("Дочки знают 20 серия👇: \n https://cloud.mail.ru/public/1J7o/PVVXNykvt ",
                                         reply_markup=select_another_keyboard_know())
