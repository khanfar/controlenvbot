import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up basic logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Load .env file
load_dotenv()

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("MY_TELEGRAM_BOT_TOKEN")

# Function to read allowed user IDs and budgets directly from .env file
def read_allowed_users_and_budgets():
    allowed_users = []
    budgets = []
    with open('.env', 'r') as file:
        for line in file:
            if line.startswith('ALLOWED_TELEGRAM_USER_IDS'):
                allowed_users = line.strip().split('=')[1].split(',')
            elif line.startswith('USER_BUDGETS'):
                budgets = line.strip().split('=')[1].split(',')
    return allowed_users, budgets


# Function to update .env file
def update_env_file(allowed_users, budgets):
    env_lines = []
    with open('.env', 'r') as file:
        for line in file:
            if line.startswith('ALLOWED_TELEGRAM_USER_IDS'):
                env_lines.append(f"ALLOWED_TELEGRAM_USER_IDS={','.join(allowed_users)}\n")
            elif line.startswith('USER_BUDGETS'):
                env_lines.append(f"USER_BUDGETS={','.join(budgets)}\n")
            else:
                env_lines.append(line)

    with open('.env', 'w') as file:
        file.writelines(env_lines)

# Command to display allowed users and budgets
def show_allowed_users(update: Update, context: CallbackContext):
    allowed_users, budgets = read_allowed_users_and_budgets()
    message = "Allowed Users and Budgets:\n"
    for user, budget in zip(allowed_users, budgets):
        message += f"User: {user}, Budget: {budget}\n"
    update.message.reply_text(message)

# Command to add a new user
def add_user(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        update.message.reply_text("Usage: /adduser <user_id> <budget>")
        return

    new_user = context.args[0]
    new_budget = context.args[1]
    allowed_users, budgets = read_allowed_users_and_budgets()

    if new_user in allowed_users:
        update.message.reply_text("User already exists.")
        return

    allowed_users.append(new_user)
    budgets.append(new_budget)
    update_env_file(allowed_users, budgets)
    update.message.reply_text("User added successfully.")

# Command to delete a user
def delete_user(update: Update, context: CallbackContext):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /deleteuser <user_id>")
        return

    user_to_delete = context.args[0]
    allowed_users, budgets = read_allowed_users_and_budgets()

    if user_to_delete in allowed_users:
        index = allowed_users.index(user_to_delete)
        allowed_users.pop(index)
        budgets.pop(index)
        update_env_file(allowed_users, budgets)
        update.message.reply_text("User deleted successfully.")
    else:
        update.message.reply_text("User not found.")

# Command to edit a user's budget
def edit_user_budget(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        update.message.reply_text("Usage: /editbudget <user_id> <new_budget>")
        return

    user_to_edit = context.args[0]
    new_budget = context.args[1]
    allowed_users, budgets = read_allowed_users_and_budgets()

    if user_to_edit in allowed_users:
        index = allowed_users.index(user_to_edit)
        budgets[index] = new_budget
        update_env_file(allowed_users, budgets)
        update.message.reply_text("User's budget updated successfully.")
    else:
        update.message.reply_text("User not found.")

# Error handler function
def error_handler(update: Update, context: CallbackContext):
    """Log the error and send a telegram message to notify the developer."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Main function to run the bot
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("showusers", show_allowed_users, pass_args=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("adduser", add_user, pass_args=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("deleteuser", delete_user, pass_args=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("editbudget", edit_user_budget, pass_args=True, pass_chat_data=True))

    # Register the error handler
    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
