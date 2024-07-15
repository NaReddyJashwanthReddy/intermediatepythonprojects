from dotenv import load_dotenv
import os
from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler 
from telegram.ext.filters import Filters 

load_dotenv()
Token=os.getenv('TOKEN')

updater=Updater(token=Token,use_context=True)

def start(Update : Update, context:CallbackContext):
    Update.message.reply_text(
        r"hello sir/mam , welcome to the Bot.Please write /help to see the commands available."
    )
    
def help(Update:Update,context:CallbackContext):
    Update.message.reply_text(
    """Available Commands :- 
    /youtube - To get the youtube URL 
    /linkedin - To get the LinkedIn profile URL 
    /gmail - To get gmail URL 
    /insta - To get the Instagram URL
    """
    )
    
def email_url(Update:Update,context:CallbackContext):
    Update.message.reply_text(
        "E-mail address link here"
    )
    
def youtube_url(Update:Update,context:CallbackContext):
    Update.message.reply_text(
        r"Youtube Link=>  https://www.youtube.com/"
    )
    
def linkdin_url(Update:Update,context:CallbackContext):
    Update.message.reply_text(
        r"Linkdin Link =>  https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/"
    )
    
def insta_url(Update:Update,context:CallbackContext):
    Update.message.reply_text(
        r"Insta link here =>  https://www.instagram.com/"
    )
    
def unknown(Update:Update,context:CallbackContext):
    Update.message.reply_text(
        "sorry '%s' is not a valid command" % Update.message.text
    )
    
def unknown_text(Update:Update,context:CallbackContext):
    Update.message.reply_text(
        "Sorry I can't recognizeyou, you said '%s'" % Update.message.text 
    )
    
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('help',help))
updater.dispatcher.add_handler(CommandHandler('youtube',youtube_url))
updater.dispatcher.add_handler(CommandHandler('email',email_url))
updater.dispatcher.add_handler(CommandHandler('linkdin',linkdin_url))
updater.dispatcher.add_handler(CommandHandler('insta',insta_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text,unknown_text))
updater.dispatcher.add_handler(MessageHandler(Filters.command,unknown))

updater.start_polling()
updater.idle()

