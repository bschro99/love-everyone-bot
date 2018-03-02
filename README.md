# Love Everyone Bot

The "Love Everyone Bot" is a Twitter bot that tweets positive messages every ~15 minutes to anyone who has been using hashtags like #depressed, #suicidal, etc. You can see the bot in action here: https://www.twitter.com/loveeveryonebot
Note: The bot was banned within it's first day for spamming. According to Twitter rules, "You may not use the Twitter service for the purpose of spamming anyone", including sending "large numbers of unsolicited replies or mentions". I warned you.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to be able to run this bot, you're going to need:
- Python 3.x
- The Tweepy library
- A Twitter Account
```
Python: If you don't already have python downloaded, please see this: https://wiki.python.org/moin/BeginnersGuide/Download
Tweepy Library: See "Installing"
Twitter: Sign up on https://www.twitter.com
```
- Twitter App:
You're going to need a Twitter Account that is *connected to a phone number.* This is required for remotely posting.


### Installing

A step by step series of examples that tell you have to get a development environment running

**Installing Tweepy**

The easiest way to install the latest version is by using pip/easy_install to pull it from PyPI:
```
pip install Tweepy
```

You can also use the Tweepy Git to clone the repository from GitHub and install it manually:
```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python setup.py install
```


**Creating a Twitter Application**

- Login in to your Twitter account that is connected to a phone number
- Go to https://www.apps.twitter.com
- Create a new app
```
Name: Whatever you want it to be
Description: Desc.
Website: This can be a placeholder 
Callback URL: You can ignore this
```

- Once you've created your application, go it's settings and in the "access level" section, select "Read and write"
- Click on "Manage keys and tokens" and copy:
  - Access Token
  - Secret Access Token
  - Consumer Key
  - Secret Consumer Key


**Running the bot**

Open the file "credentials.py" with a text editor and paste your access token, consumer key, etc.
It should look like this:
```
#Import Tweepy
import tweepy

consumer_key = 'Consumer Key you copied from Twitter'
consumer_secret = 'Secret Consumer Key you copied from Twitter'
access_token = 'Access Token you copied from Twitter'
access_token_secret = 'Secret Access Token you copied from Twitter'
```

To test it, run "i-love-everyone-bot-test.py"
```
python i-love-everyone-bot-test.py
```
If it all works, something like this should a output:
```
@bs_bites Your smile makes the universe happy #LoveEveryoneBot
```

If that works, you can then run the "i-love-everyone-bot.py":
```
python i-love-everyone-bot.py
```
This should post on your Twitter!

*WARNING: SPAMMING AND UNSOLICITED @MENTIONS IS AGAINST TWITTER'S RULES. WATCH OUT*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

