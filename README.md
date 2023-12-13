

![Screenshot_20231212_001558_TurboTel~2](https://github.com/khanfar/controlenvbot/assets/16803586/de08b7de-1360-4bff-8940-b8bc74a1dd26)



PLEASE USE LAST VERSION V4 


you need to put the python file in same env file location .


you need to add this line up in env file :

MY_TELEGRAM_BOT_TOKEN=594xxxx413:AAEC8xxxxxLuw9XEMlPA

so you put telegram bot token so you in that bot can use to show or add users id and there budgets 


to show users list just type : /showusers


to add user use like this : /adduser 123456789 50      


so you will add user with id /adduser 123456789 and his balance is 50$ and so on


after add user you need to restart the main.py bot 


Install Necessary Packages:


pip install python-telegram-bot python-dotenv



this env bot need to install python 13 , i use virtual enviroment to do that in windows 11 like this : 


go to same env directory and open terminal and do this :

python -m venv myenv

myenv\Scripts\activate  # On Windows

pip install python-telegram-bot==13.0

then run the envbot.py

ON V2 : 

This script now includes the commands /adduser, /deleteuser, and /editbudget, along with the original /showusers command. Each command has basic error handling and usage instructions


on v3 updated :   

Features and Functionalities:

Manage Allowed Users and Budgets:

The bot maintains a list of allowed Telegram user IDs and their corresponding budgets. This information is stored and managed in a .env file.

Dynamic User Interaction:

Users can interact with the bot through specific commands sent in a Telegram chat. The bot processes these commands and performs the requested actions.

Commands:

/showusers: Displays the list of currently allowed users along with their budgets.

/adduser <user_id> <budget>: Adds a new user with the specified Telegram user ID and budget to the list. If the user already exists, it notifies the sender.

/deleteuser <user_id>: Removes an existing user from the list based on the provided user ID.

/editbudget <user_id> <new_budget>: Updates the budget for an existing user.

Real-Time Updates:

Changes made through these commands are reflected in real-time in the .env file, ensuring that the bot's data is always up to date.


Error Handling:


The bot includes basic error handling to log unexpected issues and inform the user if something goes wrong.

Logging:

It uses Python's logging module to log important events and errors, which can be helpful for debugging and monitoring the bot's activity.


in v4   i add buttons in bot 


***************************************************
FOR VERSION V5  
***************************************************

YOU NEED TO ADD IN ENV FILE :    Open your .env file and make sure it has a line like this put your telegram id :


ADMIN_ID=815xxxxx

so in env file you have :

MY_TELEGRAM_BOT_TOKEN=594xxxx413:AAEC8xxxxxLuw9XEMlPA

ADMIN_ID=815xxxxx


so these need to put in env to use this v5 bot

whats new in this version 5 :

1- you see all activities in terminal    2- you will get message that bot is run 3- bug fixes


