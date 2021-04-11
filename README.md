# ClassRemind

## What is it

ClassRemind is a simple python script which sends you reminders of your online classes, along with the link of the class. 

## How to use

You need your own Telegram Bot Token to use ClassRemind. Once you have that, replace `YOUR_TOKEN` and `YOUR_ID` with your Telegram Bot Token and your Telegram user id respectively. If you don't know how to do that, or don't understand what a token is, read [this](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token) guide

## Format of Schedule.json and Subjects.json

The `Schedule.json` should be in the following format

```
{
  "Monday":{
    "SubjectCode":"StartTime-EndTime",
    "SubjectCode2":"StartTime-StartTime"
  }
  ...
}
```
Note: `StartTime` and `EndTime` are supposed to be in the ISO Time format, ie `[hh]:[mm]:[ss]` where 
1. `[hh]` refers to a zero-padded hour between 00 and 23.
2. `[mm]` refers to a zero-padded minute between 00 and 59.
3. `[ss]` refers to a zero-padded second between 00 and 60 (where 60 is only used to denote an added leap second).

The `Subjects.json` should be in the following format

```
{
  "SubjectCode1":{
    "name":"Expanded Name",
    "link":"Class Link 1"
  },
  "SubjectCode2":{
    "name":"Expanded Name",
    "link":"Class Link 2"
  }
  
}
```

Both the directories should be in the same directory as `Main.py`

## Dependencies

1. [python-telegram-bot](https://python-telegram-bot.org/)
4. [pytz](https://pypi.org/project/pytz/)
