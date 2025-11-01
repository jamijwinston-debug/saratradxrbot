import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot token (you'll need to set this as an environment variable)
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a button that shows the main content when clicked."""
    keyboard = [
        [InlineKeyboardButton("Show Content", callback_data="show_content")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to the Trading Bot! Click the button below to see our amazing offers.",
        reply_markup=reply_markup
    )

# Button callback handler
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == "show_content":
        # Send the image with caption
        image_url = "https://via.placeholder.com/400x200/4A90E2/FFFFFF?text=Trading+Signals"  # Replace with your actual image URL
        
        try:
            # Send image with caption
            await query.message.reply_photo(
                photo=image_url,
                caption=get_trading_content(),
                parse_mode='HTML'
            )
        except Exception as e:
            logger.error(f"Error sending image: {e}")
            # Fallback: send text only if image fails
            await query.message.reply_text(
                get_trading_content(),
                parse_mode='HTML'
            )
    
    elif query.data == "show_done":
        await query.message.reply_text(get_done_content())

# Function to get trading content
def get_trading_content():
    return """🌐 <b>If You Are A Trader and want To Make Profit Then Welcome To Our Community!</b> 🔥

We will help You To Recover Your Losses, Just Join our 20$ To 2000$ Compounding Session Daily 💵

🔷 99% Accuracy
🔷 Loss Recovery
🔷 Non Mtg Signals
🔷 Daily 10 to 15 Sureshot Signals
🔷 Expert Trading Signals
🔷 Community Support
🔷 24/7 Assistance

🙋‍♂️ Let's make profitable trades together!

💥 <b>Join the Winning Team NOW!</b> 💥
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️

https://t.me/+JBiO5pr6629mOTI1

https://t.me/+JBiO5pr6629mOTI1"""

# Function to get done content
def get_done_content():
    return """✅ <b>Done! Congratulations on your new bot.</b>

Use this token to access the HTTP API:
<code>8509238155:AAF282n8AqEaFh8yCezm4HBZqOT6UFFE8KA</code>

⚠️ <i>Keep your token secure and store it safely, it can be used by anyone to control your bot.</i>

For a description of the Bot API, see this page: 
https://core.telegram.org/bots/api"""

# Done command handler (alternative way to show done content)
async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show the done message directly."""
    await update.message.reply_text(
        get_done_content(),
        parse_mode='HTML'
    )

# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f"Exception while handling an update: {context.error}")

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("done", done))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_error_handler(error_handler)

    # Start the Bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
