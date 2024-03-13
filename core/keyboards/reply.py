from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1. Кнопка 1',
        ),
        KeyboardButton(
            text='Ряд 1. Кнпока 2 '
        ),
        KeyboardButton(
            text='Ряд 1. Кнопка 3'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 2. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 3'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 4'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 3. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 3.Кнопка 2'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку⬇', selective=True)

# для того чтобы клавиатуру сделать компактной, нужно указать
# resize_keyboard значение true one_time_keyboard позволяет скрывать
# клавиатуру после первого нажатия пользователя на одну из кнопок
# input_field_placeholder показывает подсказку для пользователя в поле ввода
# сообщения selective показывает клавиатуру только тому пользователю,кто ее
# запросил.Данный аргумент актуален только если вы используете бота в группе


loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Отправь геолокацию',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Отправь свой контакт',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Создать викторину',
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False,
    input_field_placeholder='Отправь локацию, номер телефона или создай викторну/опрос ⬇' )



