you need to put the python file in same env file location .
you need to add this line up in env file :

MY_TELEGRAM_BOT_TOKEN=594xxxx413:AAEC8xxxxxLuw9XEMlPA

so you put telegram bot token so you in that bot can use to show or add users id and there budgets 
to show users list just type : /showusers
to add user use like this : /adduser 123456789 50      
so you will add user with id /adduser 123456789 and his balance is 50$ and so on

after add user you need to restart the main.py bot 

this env bot need to install python 13 , i use virtual enviroment to do that in windows 11 like this : 

go to same env directory and open terminal and do this :
python -m venv myenv
myenv\Scripts\activate  # On Windows
pip install python-telegram-bot==13.0

then run the envbot.py

