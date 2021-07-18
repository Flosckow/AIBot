from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import apiai
import json
updater = Updater(token='1846546104:AAFyZnhpTnI8QfB8DMaRuvxNi3QIKGIHR10') # Токен API к Telegram
dispatcher = updater.dispatcher

# https://habr.com/ru/post/346606/

# key dialogflow:  88e15a64cd4c0c495f3fbf92f39905b4e5311075



GOOGLE_APPLICATION_CREDENTIALS="C:/Users/admin/Downloads/small-talk-ygsm-92ea4ce2a54c.json"




def startCommand(update, context):
    update.message.reply_text('Привет, давай пообщаемся?')


def textMessage(update: Update, context: CallbackContext):
    request = apiai.ApiAI('92ea4ce2a54cd4e5cda660d06c1370ff34104cfe').text_request()
    request.lang = 'ru'
    request.session_id = 'DanielBotAI'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))

    response = responseJson['result']['fulfillment']['speech']
    print(response)

    if response:
        update.message.reply_text(response)
    else:
        update.message.reply_text('Я Вас не совсем понял!')


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()