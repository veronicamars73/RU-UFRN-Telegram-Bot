from scrapper.scrapper import get_almoco, get_cardapio, get_janta
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


updater = Updater("5518994838:AAF4JtwQ9dsqBuCNUuRTgwK2BYadxRJlON4",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Eu sou o RU Bot. Você pode me usar para descobrir o cardápio do dia do RU da UFRN.")
    

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Para me usar você pode solicitar o cardápio do dia usando o comando /cardapio, o cardápio do almoço com /almoco e o cardápio do jantar com /jantar.")

def almoco(update: Update, context: CallbackContext):
    almoco = get_almoco()
    update.message.reply_text("Almoço\nProteínas:\n"+ almoco[0][0][0]+"\nAcompanhamentos:\n"+almoco[0][1][0]+"\n"+("-"*30)+"\nVegetariano:\n"+almoco[1][0][0])
    
def jantar(update: Update, context: CallbackContext):
    janta = get_janta()
    update.message.reply_text("Jantar\nProteínas:\n"+janta[0][0][0]+"\nAcompanhamentos:\n"+janta[0][1][0]+"\n"+("-"*30)+"\nVegetariano:\n"+janta[1][0][0])
    
def cardapio(update: Update, context: CallbackContext):
    cardapio = get_cardapio()
    update.message.reply_text("Almoço\nProteínas:\n"+ cardapio[0][0][0]+"\nAcompanhamentos:\n"+cardapio[0][1][0]+"\n"+("-"*30)+"\nVegetariano:\n"+cardapio[1][0][0])
    update.message.reply_text("Jantar\nProteínas:\n"+cardapio[2][0][0]+"\nAcompanhamentos:\n"+cardapio[2][1][0]+"\n"+("-"*30)+"\nVegetariano:\n"+cardapio[3][0][0])

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Desculpa '%s' não é um comando válido" % update.message.text)
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Desculpa, não reconheço '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('almoco', almoco))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('jantar', jantar))
updater.dispatcher.add_handler(CommandHandler('cardapio', cardapio))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()