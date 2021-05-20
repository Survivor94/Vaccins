import telegram
import keys
import time

# Message
msg = "" 

# Send the actual message to the analyst
def send(msg, chatid, token):
    bot = telegram.Bot(token)
    bot.sendMessage(chatid, msg)

# Initialize the components to be send
def initiateChat(codes):
    msg = "Vaccinatiemogelijkheid gevonden voor "+codes+", ga snel naar https://www.prullenbakvaccin.nl/. Volgende melding komt over minimaal 1 uur."
    
    # Start the messaging sequence
    send(msg, keys.chatID, keys.token)

    