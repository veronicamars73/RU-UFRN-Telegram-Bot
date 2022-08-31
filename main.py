import datetime, pytz


from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from scrapper.scrapper import get_almoco, get_cardapio, get_cardapio_string, get_janta


updater = Updater("5518994838:AAF4JtwQ9dsqBuCNUuRTgwK2BYadxRJlON4",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Eu sou o RU Bot. Você pode me usar para descobrir o cardápio do dia do RU da UFRN.")
    
def help(update: Update, context: CallbackContext):
    update.message.reply_text("Para me usar você pode solicitar o cardápio do dia usando o comando /cardapio, o cardápio do almoço com /almoco e o cardápio do jantar com /jantar. Para um lembrete diário execute o comando /lembrete.")

def lembrete(update: Update, context: CallbackContext):
    context.job_queue.run_daily(msg,datetime.time(hour=9, minute=00, tzinfo=pytz.timezone('America/Sao_Paulo')),
                                days=(0, 1, 2, 3, 4, 5, 6), context=update.message.chat_id)
    update.message.reply_text("Lembrete diário criado!")

def almoco(update: Update, context: CallbackContext):
    almoco = get_almoco()
    update.message.reply_text("Almoço\nProteínas:\n"+ almoco[0][0]+"\nAcompanhamentos:\n"+almoco[0][1]+"\n"+("-"*30)+"\nVegetariano:\n"+almoco[1][0])
    
def jantar(update: Update, context: CallbackContext):
    janta = get_janta()
    update.message.reply_text("Jantar\nProteínas:\n"+janta[0][0]+"\nAcompanhamentos:\n"+janta[0][1]+"\n"+("-"*30)+"\nVegetariano:\n"+janta[1][0])
    
def cardapio(update: Update, context: CallbackContext):
    cardapio = get_cardapio()
    update.message.reply_text("Almoço\nProteínas:\n"+ cardapio[0][0]+"\nAcompanhamentos:\n"+cardapio[0][1]+"\n"+("-"*30)+"\nVegetariano:\n"+cardapio[1][0])
    update.message.reply_text("Jantar\nProteínas:\n"+cardapio[2][0]+"\nAcompanhamentos:\n"+cardapio[2][1]+"\n"+("-"*30)+"\nVegetariano:\n"+cardapio[3][0])

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Desculpa '%s' não é um comando válido" % update.message.text)
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Desculpa, não reconheço '%s'" % update.message.text)
    
def msg(context):
    context.bot.send_message(chat_id=context.job.context, text=get_cardapio_string())

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('almoco', almoco))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('lembrete', lembrete))
updater.dispatcher.add_handler(CommandHandler('jantar', jantar))
updater.dispatcher.add_handler(CommandHandler('cardapio', cardapio))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
updater.idle()