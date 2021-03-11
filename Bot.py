import time
import telegram #library to make interacting with telegram API easier
from flask import Flask, request
from creds import bot_token,bot_username,URL # your credentials for telegram bot
from Abilities import lookup #your bots abilities

global bot
global TOKEN
TOKEN=bot_token
bot=telegram.Bot(token=TOKEN)
app=Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   update=telegram.Update.de_json(request.get_json(force=True), bot)
   chat_id=update.message.chat.id
   msg_id=update.message.message_id
   text=update.message.text.encode('utf-8').decode()
   if text.lower() in ['/start','hello']: # you can have as many greeting as you like in the list
       bot_welcome_msg='Hello\nWhich file are you looking for?'
       bot.sendChatAction(chat_id=chat_id, action="typing") # to make the bot more realistic added a time delay and typing action
       time.sleep(1.5) #time delay
       bot.sendMessage(chat_id=chat_id, text=bot_welcome_msg, reply_to_message_id=msg_id)
   else:
       try:
           bot.sendMessage(chat_id=chat_id, text=lookup(text.capitalize()), reply_to_message_id=msg_id) #search for file in database using lookup function
       except Exception:
           bot.sendMessage(chat_id=chat_id, text="Oops, something went wrong, please try again later", reply_to_message_id=msg_id) # if error occurs you will know
   return 'ok'

@app.route('/start_bot', methods=['GET', 'POST'])
def set_webhook(): #setting up webhook so that the bot can communicate with scripts
   s=bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if s:
       return "Bot Activated"
   else:
       return "Setup Failed"

@app.route('/')
def index():
   return 'To start bot type /start_bot in url'

if __name__ == '__main__':
   app.run(threaded=True)
