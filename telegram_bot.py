import telebot

# https://t.me/efefeefefeffbot
bot = telebot.TeleBot("5861301555:AAHJJCY73wbsz0ZlPjSiYoco5zrQ1DhyEmA", parse_mode=None)
money_bank = [100]


@bot.message_handler(content_types=["text"])
def send_welcome(message):
    money = message.text
    if money == '1':
        if money_bank[0] >= 1:
            money_bank[0] = money_bank[0] - 1
            print("Осталось денег: " + str(money_bank[0]))
            bot.send_message(message.chat.id, f"{message.from_user.full_name}, Заберите ваш чай")
        else:
            bot.send_message(message.chat.id, "Нету денег")
    elif money == '2':
        if money_bank[0] >= 2:
            money_bank[0] = money_bank[0] - 2
            print("Осталось денег: " + str(money_bank[0]))
            bot.send_message(message.chat.id, f"{message.from_user.full_name}, Заберите ваш Американо")
        else:
            bot.send_message(message.chat.id, "Нету денег")
    elif money == '3':
        if money_bank[0] >= 3:
            money_bank[0] = money_bank[0] - 3
            print("Осталось денег: " + str(money_bank[0]))
            bot.send_message(message.chat.id, f"{message.from_user.full_name}, Заберите ваш Латте")
        else:
            bot.send_message(message.chat.id, "Нету денег")
    else:
        print("Осталось денег: " + str(money_bank[0]))
        bot.send_message(message.chat.id, f"{message.from_user.full_name}, Вы ввели ерунду")


bot.infinity_polling()