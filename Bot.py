import telebot
from random import randint
from telebot import types




bot = telebot.TeleBot(token="") # Здесь вставляем свой токен

main_menu_reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
main_menu_reply_markup.row(
    types.KeyboardButton(text="🪨"), types.KeyboardButton(text="✂"), types.KeyboardButton(text="📃"))

@bot.message_handler(commands=['start'])
def start_message_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    # не забываем прикрепить объект клавиатуры к сообщению
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет!\n Давай поиграем в камень ножницы бумага! "\
        "Сделай свой ход 👇🏻",
        reply_markup=main_menu_reply_markup
    )
@bot.message_handler(content_types=["text"])
def send(message):
    responds = ["🪨", "✂", "📃"]
    a=responds[randint(0,2)]
    if message.text in responds:
        bot.send_message(message.chat.id, a)
        players_move=message.text
        bot_move=a
        gameplay={"🪨":"✂",
                   "✂":"📃",
                   "📃":"🪨"}
        if players_move == bot_move:
                bot.send_message(message.chat.id,"ничья")

        for i, j in gameplay.items():
            if players_move == i and bot_move == j:
                bot.send_message(message.chat.id,"Вы победили")
                break
            elif bot_move == i and players_move == j:
                bot.send_message(message.chat.id,"Я победил")
                break



def main():
    # запускаем нашего бота
    bot.infinity_polling()

if __name__ == '__main__':
    main()