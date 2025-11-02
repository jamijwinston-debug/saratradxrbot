import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Image URL
IMAGE_URL = "https://freeimage.host/i/KsDHE8l"

# Main message content
MAIN_MESSAGE = """🌐 if You Are A Trader and want To Make Profit Then Welcome To Our Community! 🔥

We will help You To Recover Your Losses, Just Join our 20$ To 2000$ Compounding Session Daily 💵

🔷 99% Accuracy
🔷 Loss Recovery
🔷 Non Mtg Signals
🔷 Daily 10 to 15 Sureshot Signals
🔷 Expert Trading Signals
🔷 Community Support
🔷 24/7 Assistance
🙋‍♂️ Let's make profitable trades together!

💥 Join the Winning Team NOW! 💥
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️

https://t.me/+eabn_K2wO6kwNjQ9

https://t.me/+eabn_K2wO6kwNjQ9"""

# Completion message
COMPLETION_MESSAGE = "Done! Congratulations on your new bot."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with the image and a button when the command /start is issued."""
    
    # Create inline keyboard with button
    keyboard = [
        [InlineKeyboardButton("Click Here", callback_data="show_content")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send photo with caption and button
    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption="Click the button below to see our amazing offers! 👇",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    query = update.callback_query
    
    # Answer the callback query
    await query.answer()
    
    if query.data == "show_content":
        # Edit the original message to show completion message
        await query.edit_message_caption(caption=COMPLETION_MESSAGE)
        
        # Send the main content as a new message
        await query.message.reply_text(MAIN_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Use /start to begin!")

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Start the Bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
