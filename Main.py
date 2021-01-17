from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler,Filters
from datetime import time
from datetime import timedelta
from pytz import timezone
import json
from datetime import datetime

updater = Updater(token=YOUR_TOKEN, use_context=True)
dispatcher = updater.dispatcher
j = updater.job_queue

with open('Data.json') as f:
    days = json.load(f)

with open('Subjects.json') as f:
    subjects = json.load(f)
my_ids = [MY_ID]

def daily(context):
    for my_id in my_ids:
        context.bot.send_message(chat_id=my_id, text="Timely Reminder for " + subjects[context.job.name]['name'])
        context.bot.send_message(chat_id=my_id, text="Link: " + subjects[context.job.name]['link'])

def start(update,context):
    if update.effective_chat.id in my_ids:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You're already in the bot's list")
        print(update.effective_chat.id)
    else:
        my_ids.append(update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="You've been added to the list. The bot will remind you before every class")

dispatcher.add_handler(CommandHandler('start', start))
weekday = 1
for day in days:
    for subject in days[day]:
        start_time = datetime(2021, 1, 17+weekday,int(days[day][subject].split('-')[0]),tzinfo=timezone('Asia/Kolkata'))
        j.run_repeating(daily,interval=timedelta(days=7), first=start_time, name=subject)
    weekday += 1
updater.start_polling()
updater.idle()