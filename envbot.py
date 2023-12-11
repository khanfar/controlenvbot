import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
import telegram

# Load .env file
load_dotenv()

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("MY_TELEGRAM_BOT_TOKEN")

# Function to read allowed user IDs and budgets
def read_allowed_users_and_budgets():
    allowed_users = os.getenv("ALLOWED_TELEGRAM_USER_IDS").split(',')
    budgets = os.getenv("USER_BUDGETS").split(',')
    return allowed_users, budgets

# Command to display allowed users and budgets
def show_allowed_users(update, context):
    allowed_users, budgets = read_allowed_users_and_budgets()
    message = "Allowed Users and Budgets:\n"
    for user, budget in zip(allowed_users, budgets):
        message += f"User: {user}, Budget: {budget}\n"
    update.message.reply_text(message)

# Function to update .env file
def update_env_file(key, value):
    os.environ[key] = value
    with open('.env', 'w') as f:
        for env_key, env_value in os.environ.items():
            f.write(f"{env_key}={env_value}\n")

# Command to add a new user
def add_user(update, context):
    # Check if the correct number of arguments are provided
    if len(context.args) < 2:
        update.message.reply_text("Usage: /adduser <user_id> <budget>")
        return

    new_user = context.args[0]
    new_budget = context.args[1]

    # Additional validation can be added here (e.g., check if the user ID and budget are valid)

    allowed_users, budgets = read_allowed_users_and_budgets()
    allowed_users.append(new_user)
    budgets.append(new_budget)
    update_env_file("ALLOWED_TELEGRAM_USER_IDS", ','.join(allowed_users))
    update_env_file("USER_BUDGETS", ','.join(budgets))
    update.message.reply_text("User added successfully.")


# Main function to run the bot
def main():
    print("python-telegram-bot version:", telegram.__version__)
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("showusers", show_allowed_users, pass_args=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("adduser", add_user, pass_args=True, pass_chat_data=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
