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
try:
    with open('UserIds.data') as f:
        my_ids = f.read().strip().split(' ')
except IOError:
    my_ids = []

my_ids = list(map(lambda x: int(x), my_ids))

def daily(context):
    for my_id in my_ids:
        context.bot.send_message(chat_id=my_id, text="Reminder for " + subjects[context.job.name]['name'] + '. The class starts in 5 minutes')
        context.bot.send_message(chat_id=my_id, text="Link: " + subjects[context.job.name]['link'])

def start(update,context):
    if update.effective_chat.id in my_ids:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You're already in the bot's list")
    else:
        my_ids.append(update.effective_chat.id)
        with open('UserIds.data', 'a') as f:
            f.write(f' {update.effective_chat.id} ')
        context.bot.send_message(chat_id=update.effective_chat.id, text="You've been added to the list. The bot will remind you before every class")
def do(update, context):
    if update.effective_chat.id!=1143044528:
        return
    args = context.args
    text = ' '.join(args)
    for my_id in my_ids:
        context.bot.send_message(chat_id=my_id, text=text)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('do', do))
weekday = 0
for day in days:
    for subject in days[day]:
        start_time = datetime.strptime(days[day][subject].split('-')[0], '%H:%M:%S')
        start_time = start_time.replace(2021,1,18+weekday)
        start_time = timezone('Asia/Kolkata').localize(start_time)
        if start_time<datetime.now().astimezone(timezone('Asia/Kolkata')):
            start_time = start_time + timedelta(days=7)
        print(start_time)
        j.run_repeating(daily,interval=timedelta(days=7), first=(start_time-timedelta(minutes=5)).astimezone(timezone('UTC')), name=subject)
    weekday += 1
updater.start_polling()
updater.idle()
