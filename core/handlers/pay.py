from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
# import config


async def order(message: Message, bot: Bot):
    await  bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка через Telegram бот',
        description='Учимся принимать платежи через Telegram бот',
        payload='Payment through a bot',
        provider_token='381764678:TEST:75395',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Доступ к секретной информации',
                amount=99000
            ),
            LabeledPrice(
                label='НДС',
                amount=20000
            ),
            LabeledPrice(
                label='Скидка',
                amount=-20000
            ),
            LabeledPrice(
                label='Бонус',
                amount=-40000
            )
        ],
        max_tip_amount=5000,  # максимальная сумма чаевых
        suggested_tip_amounts=[1000, 2000, 3000, 4000],  # список предлагаемых
        # сумм для чаевых, максимум 4 элемента
        start_parameter='nztcoder',  # если оставить этот параметр пустым,
        # то когда счет на оплату перешлют в другой чат, кнопка "оплатить"
        # останется, в следствие любой сможет оплатить данный счет.Если
        # данные параметра будут не пустым, то при перессылке счета в другой
        # чат будет видна не кнопка "оплатить", а кнопка со ссылкой на бота,
        # из которого переслали данный счет
        provider_data=None,  # если платежный провайдер просит вас передавать
        # какие либо данные, то эти данные могут быть отправлены этим
        # параметром
        photo_url='',  # ссылка на картинку, которая будет отображена в счете
        photo_size=100,  # размер картинки
        photo_width=800,  # ширина картинки
        photo_height=450,  # высота картинки
        need_name=True,  # если вам нужно полное имя пользователя, то с данным
        # параметром передайте True
        need_phone_number=True,
        # если вам нужен номер телефона пользователя, то передайте True
        need_email=True,  # если вам нужен имейл пользователя, передайте true
        need_shipping_address=False,
        # если вам нужен адрес для доставки продутка, то передайте true
        send_phone_number_to_provider=False,
        # если платежный провайдер просит вас отправить ему номер телефона
        # покупателя, то передайте true
        send_email_to_provider=False,
        # если платежный провайдер просит вас отправить ему имейл
        # покупателя, то передайте true
        is_flexible=False,
        # если конечная цена зависит от способа доставки, то передайте true
        disable_notification=False,
        # передайте true, если хотите, чтобы сообщение было отправлено без
        # звука
        protect_content=False,
        # отправьте true, если нужно защитить пост от пересылки, копирования
        # и т.д.
        reply_to_message_id=None,  # если хотите отправить счет пользвателю
        # цитируя какое-либо сообщение, то укажите его id
        allow_sending_without_reply=True,  # передайте true, если хотите
        # отправить счет на оплату, даже если цитируемое сообщение не найдено
        reply_markup=None,  # если хотите отправить еще какую либо клавиатуру,
        # то сформируйте ее и отправьте данным параметром.Обращаю внимание,
        # что первая кнопка должна быть "оплатить"
        request_timeout=15  # после того как пользователь запросит счет,
        # введет свои данные и введет данные карты, мы долдны подтвердить,
        # что готовы выслать пользователю покупаемый продукт
    )


async def pre_checkout_query( pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def succesful_payment(message: Message):
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'\
          f'\r\nНаш менеджер получил заявку и уже набирает Ваш номер телефона.'\
          f'\r\nПока можете скачать цифровую версию продукта'
    await message.answer(msg)

