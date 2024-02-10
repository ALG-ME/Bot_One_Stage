import telebot
bot = telebot.TeleBot('тут токен')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'как дела':
        bot.reply_to(message, f'Нормально, мой разраб пока меня учит.. а твои как?')  # Ответ перессылкой на пердыдущее сообщение
    else:
        bot.reply_to(message, message.text)


# Инициализация запуска (Бесконечного)
bot.infinity_polling()
