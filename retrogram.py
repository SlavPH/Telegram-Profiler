#!/usr/bin/env python3

## TELEGRAM PROFILER BOT
## BY GOTHPH

## IMPORTS
import telebot
import time
import sys
import csv

## LOCKER
status = False

def lock():
    global status
    status = True

def unlock():
    global status
    status = False

## TELEGRAM PROFILER FUNCTION
def Telegram(cid):
    directories = [
        'newaa','newab','newac','newad','newae','newaf','newag','newah',
        'newai','newag','newak','newal','newam','newan','newao','newap',
        'newaq','newar','newas','newat','newau','newav','newaw','newax',
        'neway','newaz','newba','newbb','newbc','newbd','newbe','newbf',
        'newbg','newbh','newbi','newbj','newbk','newbl','newbm','newbn',
        'newbo','newbp','newbq','newbr','newbs','newbt','newbu','newbv'
        ]
    for directory in directories:
        with open(directory, 'r') as data:
            csvreader = csv.reader(data)
            for row in csvreader:
                if row[0] == cid:
                    return row[1]
                    break

## DEFINING BOT
Token = "5611561145:AAG5Avhre_Q3XHo0mRK2geWcvqUTvi7NeOQ"
bot = telebot.TeleBot(Token)


## START COMMAND
@bot.message_handler(commands=['start'])
def start_command(message):
    user = message.from_user.first_name
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, f"Hello {user}! Send Chat-ID")

## PING COMMAND
@bot.message_handler(commands=['ping'])
def start_command(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Running perfectly")

## MESSAGE HANDLER
@bot.message_handler(func = lambda message: message.text.isnumeric())
def all_handler(message):
    global status

    if status == False:
        cid = message.text.strip()
        msg1 = bot.reply_to(message, "[+] Fetching... It can take up to a minute!")
        try:
            lock()
            result = Telegram(cid)
            if result == None:
                bot.edit_message_text(text="[+] Target not found", chat_id=message.chat.id, message_id=msg1.message_id)
                unlock()
            else:
                bot.edit_message_text(text=f"""
# BrainSec !@#$
#-----> id = {cid}
#-----> Number = +{result}
#-----> Link1 = t.me/+{result}
#-----> Link2 = tg://user?id={cid}
""", chat_id=message.chat.id, message_id=msg1.message_id, disable_web_page_preview=True)
                unlock()
        except:
            bot.edit_message_text(text="[+] Process failed! Do it again.", chat_id=message.chat.id, message_id=msg1.message_id)
            unlock()
    else:
        bot.send_chat_action(message.chat.id, "typing")
        bot.reply_to(message, "Another user is using this process!")

## RUN THE BOT
bot.infinity_polling(skip_pending=True)
