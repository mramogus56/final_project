import telebot
from ai_logic import get_class

token = "7730286632:AAFF6_5VQ5nDnM5XDKC9KSutqvW4j5lwE84"

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я подскажу что делать, если наступило глобальное потепление. Что такое глобальное потепление? - /chto_eto\n Что у вас случилось?\n Сильная жара - /zhara\n Много пожаров - /mnogo_pozarov\n Проблемы со связью - /problemi_so_svyazy\n Землетресение - /zemletrisenie\n Наводнение - /navodnenie")

@bot.message_handler(commands=['zhara'])
def send_hello(message):
    bot.reply_to(message, "В спасении, возможно, вам поможет данная информация:\n https://zdesapteka.ru/articles/8-sovetov-kak-spastis-ot-zhary/")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Что такое глобальное потепление? - /chto_eto\n Много пожаров - /mnogo_pozarov\n Проблемы со связью - /problemi_so_svyazy\n Землетресение - /zemletrisenie\n Наводнение - /navodnenie")

@bot.message_handler(commands=['mnogo_pozarov'])
def send_hello(message):
    bot.reply_to(message, "В спасении, возможно, вам поможет данная информация:\n https://proaktive.ru/stati/chto-delat-pri-pozhare/")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Что такое глобальное потепление? - /chto_eto\n Сильная жара - /zhara\n Проблемы со связью - /problemi_so_svyazy\n Землетресение - /zemletrisenie\n Наводнение - /navodnenie")

@bot.message_handler(commands=['problemi_so_svyazy'])
def send_bye(message):
    bot.reply_to(message, "В спасении, возможно, вам поможет данная информация:\n /kak_podgotovitsya ,\n /kak_deistvovat")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Что такое глобальное потепление? - /chto_eto\n Сильная жара - /zhara\n Много пожаров - /mnogo_pozarov\n Землетресение - /zemletrisenie\n Наводнение - /navodnenie")

@bot.message_handler(commands=['kak_podgotovitsya'])
def send_bye(message):
    bot.reply_to(message, "Как подготовиться к перебоям в оказании услуг связи.\n Выясните, какие используемые в доме устройства зависят от электричества и передачи данных (телевизор, радио, маршрутизатор WiFi, стационарный телефон и т. п.). Запишите в определенном месте телефонные номера самых важных людей, с которыми может возникнуть необходимость связаться в кризисной ситуации (члены семьи, близкие, соседи, номера экстренной помощи и информационные номера). Контакты в памяти мобильного телефона станут недоступны, если аккумулятор разрядится.\n Запаситесь источниками энергии, которые можно использовать для поддержания работы различных устройств, например батарейками, аккумуляторами, аккумуляторным блоком, аккумуляторным блоком с солнечной батареей, вращаемой динамо-машиной, или запаситесь радиоприемником, работающим от батареек или аккумулятора.\n Помимо домашней интернет-сети, зависящей от электричества, приобретите мобильный интернет для смарт-устройств.\n Храните дома необходимое количество наличных денег.\n Выясните, где находятся ближайшие места, куда вы можете прийти в случае перебоев со связью: спасательная команда, полицейский участок, отделение скорой помощи, больница и т. д.")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Что такое глобальное потепление? - /chto_eto\n Сильная жара - /zhara\n Много пожаров - /mnogo_pozarov\n Землетресение - /zemletrisenie\n Наводнение - /navodnenie")

@bot.message_handler(commands=['kak_deistvovat'])
def send_bye(message):
    bot.reply_to(message, "Как действовать в случае перебоев в оказании услуг связи.\n В случае массовых перебоев с электроснабжением или мобильной передачей данных не звоните понапрасну и не нагружайте устройства. Общайтесь только в случае крайней необходимости.\n Выключите в смарт-устройствах функции, которые разряжают аккумулятор (перейдите в режим “power save mode”).\n Слушайте по радио ежечасные новости.\n Продумайте, могут ли ваши близкие или знакомые нуждаться в помощи в кризисной ситуации, и договоритесь с ними о поддержании связи между собой. Для вызова помощи во время перебоев со связью отправляйтесь сами или отправьте кого-либо в ближайшую службу спасения, полицейский участок, отделение скорой помощи или больницу.")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Что такое глобальное потепление? - /chto_eto\n Сильная жара - /zhara\n Много пожаров - /mnogo_pozarov\n Землетресение - /zemletrisenie\n Наводнение - /navodnenie")

@bot.message_handler(commands=['zemletrisenie'])
def send_bye(message):
    bot.reply_to(message, "В спасении, возможно, вам поможет данная информация:\n https://38.mchs.gov.ru/deyatelnost/poleznaya-informaciya/rekomendacii-naseleniyu/deystviya-pri-zemletryasenii")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Что такое глобальное потепление? - /chto_eto\n Сильная жара - /zhara\n Много пожаров - /mnogo_pozarov\n Проблемы со связью - /problemi_so_svyazy\n Наводнение - /navodnenie")

@bot.message_handler(commands=['chto_eto'])
def send_bye(message):
    bot.reply_to(message, "Что такое глобальное потепление:\n https://ru.wikipedia.org/wiki/Глобальное_потепление")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Сильная жара - /zhara\n Много пожаров - /mnogo_pozarov\n Проблемы со связью - /problemi_so_svyazy\n Землетресение - /zemletrisenie\n Наводнение - /navodnenie")

@bot.message_handler(commands=['navodnenie'])
def send_bye(message):
    bot.reply_to(message, "В спасении, возможно, вам поможет данная информация:\n https://lifehacker.ru/chto-dedat-pri-navodnenii/ ,\n https://38.mchs.gov.ru/deyatelnost/poleznaya-informaciya/rekomendacii-naseleniyu/deystviya-pri-navodnenii-pavodke")
    bot.reply_to(message, "Также, вам может быть полезна данная информация:\n Что такое глобальное потепление? - /chto_eto\n Сильная жара - /zhara\n Много пожаров - /mnogo_pozarov\n Проблемы со связью - /problemi_so_svyazy\n Землетресение - /zemletrisenie")

# Запускаем бота
bot.polling()