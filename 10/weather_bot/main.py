from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import config as cf
import operations as ots

updater = Updater(token=cf.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

input_handler = MessageHandler(Filters.text & (~Filters.command), ots.input_text)
dispatcher.add_handler(input_handler) 

start_handler = CommandHandler('start', ots.send_welcome)
dispatcher.add_handler(start_handler)                            

updater.start_polling()
updater.idle()