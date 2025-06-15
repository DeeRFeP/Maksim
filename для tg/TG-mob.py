from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import asyncio

TOKEN = '8044601107:AAG3cVeSZuS2pmFCOiMeh6ilwSCWd6RT0qs'
YOUR_CHAT_ID = '8153617358'

# Dictionary of country codes with Russian names
country_codes = {
    '1': 'США/Канада',
    '7': 'Россия',
    '20': 'Египет',
    '27': 'Южная Африка',
    '30': 'Греция',
    '31': 'Нидерланды',
    '32': 'Бельгия',
    '33': 'Франция',
    '34': 'Испания',
    '36': 'Венгрия',
    '39': 'Италия',
    '40': 'Румыния',
    '41': 'Швейцария',
    '43': 'Австрия',
    '44': 'Великобритания',
    '45': 'Дания',
    '46': 'Швеция',
    '47': 'Норвегия',
    '48': 'Польша',
    '49': 'Германия',
    '51': 'Перу',
    '52': 'Мексика',
    '53': 'Куба',
    '54': 'Аргентина',
    '55': 'Бразилия',
    '56': 'Чили',
    '57': 'Колумбия',
    '58': 'Венесуэла',
    '60': 'Малайзия',
    '61': 'Австралия',
    '62': 'Индонезия',
    '63': 'Филиппины',
    '64': 'Новая Зеландия',
    '65': 'Сингапур',
    '66': 'Таиланд',
    '81': 'Япония',
    '82': 'Южная Корея',
    '84': 'Вьетнам',
    '86': 'Китай',
    '90': 'Турция',
    '91': 'Индия',
    '92': 'Пакистан',
    '93': 'Афганистан',
    '94': 'Шри-Ланка',
    '95': 'Мьянма',
    '98': 'Иран',
    '211': 'Южный Судан',
    '212': 'Марокко',
    '213': 'Алжир',
    '216': 'Тунис',
    '218': 'Ливия',
    '220': 'Гамбия',
    '221': 'Сенегал',
    '222': 'Мавритания',
    '223': 'Мали',
    '224': 'Гвинея',
    '225': 'Кот-д’Ивуар',
    '226': 'Буркина-Фасо',
    '227': 'Нигер',
    '228': 'Того',
    '229': 'Бенин',
    '230': 'Маврикий',
    '231': 'Либерия',
    '232': 'Сьерра-Леоне',
    '233': 'Гана',
    '234': 'Нигерия',
    '235': 'Чад',
    '236': 'Центральноафриканская Республика',
    '237': 'Камерун',
    '238': 'Кабо-Верде',
    '239': 'Сан-Томе и Принсипи',
    '240': 'Экваториальная Гвинея',
    '241': 'Габон',
    '242': 'Республика Конго',
    '243': 'Демократическая Республика Конго',
    '244': 'Ангола',
    '245': 'Гвинея-Бисау',
    '246': 'Британская территория в Индийском океане',
    '248': 'Сейшелы',
    '249': 'Судан',
    '250': 'Руанда',
    '251': 'Эфиопия',
    '252': 'Сомали',
    '253': 'Джибути',
    '254': 'Кения',
    '255': 'Танзания',
    '256': 'Уганда',
    '257': 'Бурунди',
    '258': 'Мозамбик',
    '260': 'Замбия',
    '261': 'Мадагаскар',
    '262': 'Реюньон/Майотта',
    '263': 'Зимбабве',
    '264': 'Намибия',
    '265': 'Малави',
    '266': 'Лесото',
    '267': 'Ботсвана',
    '268': 'Эсватини',
    '269': 'Коморы',
    '290': 'Остров Святой Елены',
    '291': 'Эритрея',
    '297': 'Аруба',
    '298': 'Фарерские острова',
    '299': 'Гренландия',
    '350': 'Гибралтар',
    '351': 'Португалия',
    '352': 'Люксембург',
    '353': 'Ирландия',
    '354': 'Исландия',
    '355': 'Албания',
    '356': 'Мальта',
    '357': 'Кипр',
    '358': 'Финляндия',
    '359': 'Болгария',
    '370': 'Литва',
    '371': 'Латвия',
    '372': 'Эстония',
    '373': 'Молдова',
    '374': 'Армения',
    '375': 'Беларусь',
    '376': 'Андорра',
    '377': 'Монако',
    '378': 'Сан-Марино',
    '379': 'Ватикан',
    '380': 'Украина',
    '381': 'Черногория',
    '382': 'Сербия',
    '383': 'Косово',
    '385': 'Хорватия',
    '386': 'Словения',
    '387': 'Босния и Герцеговина',
    '389': 'Северная Македония',
    '420': 'Чехия',
    '421': 'Словакия',
    '423': 'Лихтенштейн',
    '500': 'Фолклендские острова',
    '501': 'Белиз',
    '502': 'Гватемала',
    '503': 'Сальвадор',
    '504': 'Гондурас',
    '505': 'Никарагуа',
    '506': 'Коста-Рика',
    '507': 'Панама',
    '508': 'Сен-Пьер и Микелон',
    '509': 'Гаити',
    '590': 'Гваделупа',
    '591': 'Боливия',
    '592': 'Гайана',
    '593': 'Эквадор',
    '594': 'Французская Гвиана',
    '595': 'Парагвай',
    '596': 'Мартиника',
    '597': 'Суринам',
    '598': 'Уругвай',
    '599': 'Кюрасао/Карибские Нидерланды',
    '670': 'Восточный Тимор',
    '672': 'Австралийские внешние территории',
    '673': 'Бруней',
    '674': 'Науру',
    '675': 'Папуа-Новая Гвинея',
    '676': 'Тонга',
    '677': 'Соломоновы Острова',
    '678': 'Вануату',
    '679': 'Фиджи',
    '680': 'Палау',
    '681': 'Уоллис и Футуна',
    '682': 'Острова Кука',
    '683': 'Ниуэ',
    '685': 'Самоа',
    '686': 'Кирибати',
    '687': 'Новая Каледония',
    '688': 'Тувалу',
    '689': 'Французская Полинезия',
    '690': 'Токелау',
    '691': 'Микронезия',
    '692': 'Маршалловы Острова',
    '850': 'Северная Корея',
    '852': 'Гонконг',
    '853': 'Макао',
    '855': 'Камбоджа',
    '856': 'Лаос',
    '880': 'Бангладеш',
    '886': 'Тайвань',
    '960': 'Мальдивы',
    '961': 'Ливан',
    '962': 'Иордания',
    '963': 'Сирия',
    '964': 'Ирак',
    '965': 'Кувейт',
    '966': 'Саудовская Аравия',
    '967': 'Йемен',
    '968': 'Оман',
    '970': 'Палестина',
    '971': 'Объединенные Арабские Эмираты',
    '972': 'Израиль',
    '973': 'Бахрейн',
    '974': 'Катар',
    '975': 'Бутан',
    '976': 'Монголия',
    '977': 'Непал',
    '992': 'Таджикистан',
    '993': 'Туркменистан',
    '994': 'Азербайджан',
    '995': 'Грузия',
    '996': 'Киргизия',
    '998': 'Узбекистан'
}

def get_country_name(phone_number):
    # Извлечение кода страны
    if phone_number.startswith('+'):
        # Найти первый пробел или взять первые несколько цифр после '+'
        space_index = phone_number.find(' ')
        if space_index != -1:
            country_code = phone_number[1:space_index]
        else:
            # Если пробелов нет, взять первые несколько цифр (обычно код страны состоит из 1-3 цифр)
            country_code = phone_number[1:2]  # Берем только первую цифру после '+'

        # Убедимся, что мы не взяли лишние цифры
        for length in range(1, 4):
            if country_code[:length] in country_codes:
                country_code = country_code[:length]
                break
    else:
        country_code = phone_number[0:3]  # Если нет '+', берем первые три цифры

    print(f"Извлеченный код страны: {country_code}")  # Отладочное сообщение

    # Проверка наличия кода в словаре
    country_name = country_codes.get(country_code, "Недоступно")
    print(f"Название страны: {country_name}")  # Отладочное сообщение

    return country_name

class TelegramBot:
    def __init__(self):
        self.application = None

    async def run(self):
        self.application = Application.builder().token(TOKEN).build()
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(MessageHandler(filters.CONTACT, self.handle_contact))

        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()

        # Infinite waiting
        while True:
            await asyncio.sleep(3600)

    async def start(self, update: Update, context: CallbackContext):
        contact_button = KeyboardButton("📱 Отправить контакт", request_contact=True)
        reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True)
        await update.message.reply_text(
            'Привет! Нажми кнопку ниже, чтобы поделиться контактом.',
            reply_markup=reply_markup
        )

    async def handle_contact(self, update: Update, context: CallbackContext):
        user = update.message.from_user
        contact = update.message.contact

        # Get country
        country_name = get_country_name(contact.phone_number)

        # Get profile photo
        try:
            profile_photos = await context.bot.get_user_profile_photos(user.id)
            photo_file = None
            if profile_photos.total_count > 0:
                photo = profile_photos.photos[0][-1]
                photo_file = await photo.get_file()
        except Exception as e:
            print(f"Ошибка при получении фото: {e}")
            photo_file = None

        # Form user information
        user_info = (
            f"🆔 ID: {user.id}\n"
            f"👤 Имя: {user.first_name}\n"
            f"📱 Номер: {contact.phone_number}\n"
            f"🌍 Страна: {country_name}\n"
            f"🔗 Username: @{user.username if user.username else 'нет'}"
        )

        # Send to admin
        try:
            if photo_file:
                await context.bot.send_photo(
                    chat_id=YOUR_CHAT_ID,
                    photo=photo_file.file_id,
                    caption=user_info
                )
            else:
                await context.bot.send_message(
                    chat_id=YOUR_CHAT_ID,
                    text=user_info + "\n\n📷 Фото профиля: отсутствует"
                )

            # Forward the contact to the admin
            await context.bot.forward_message(
                chat_id=YOUR_CHAT_ID,
                from_chat_id=update.message.chat_id,
                message_id=update.message.message_id
            )
        except Exception as e:
            print(f"Ошибка при отправке: {e}")

        # Reply to user
        await update.message.reply_text(
            '✅ Спасибо! Ваши данные получены, ожидайте ответа.',
            reply_markup=ReplyKeyboardRemove()
        )

if __name__ == '__main__':
    bot = TelegramBot()
    asyncio.run(bot.run())
