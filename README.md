# ClassRemind

## What is it

ClassRemind is a simple python script which sends you reminders of your online classes, along with the link of the class. 

## How to use

Presently, you need your own Telegram Bot Token to use ClassRemind. Once you have that, replace `YOUR_TOKEN` and `YOUR_ID` with your Telegram Bot Token and your Telegram user id respectively. If you don't know how to do that, or don't understand what a token is, read [this](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token) guide

## Format of Schedule.json and Subjects.json

The `Schedule.json` should be in the following format

```
{
  "Monday":{
    "SubjectCode":"StartHour-EndHour",
    "SubjectCode2":"StartHour-EndHour"
  }
  ...
}
```

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

## Known Issues

Here are some of the issues we're aware of, and are working to resolve :-

1. Time should be specified in ISO Time Format for better usability
2. A single Bot should function for multiple users, storing each users Schedule. Presently each user has to create their own instance of the bot. 
