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

# Get bot token from environment variable or use default
BOT_TOKEN = os.getenv('BOT_TOKEN', '8509238155:AAF282n8AqEaFh8yCezm4HBZqOT6UFFE8KA')

# Log token status (without exposing full token)
if os.getenv('BOT_TOKEN'):
    logger.info("Using BOT_TOKEN from environment variable")
else:
    logger.info("Using default BOT_TOKEN from code")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    try:
        user = update.effective_user
        logger.info(f"Start command received from user: {user.id if user else 'Unknown'}")
        
        keyboard = [
            [InlineKeyboardButton("Show Content", callback_data="show_content")],
            [InlineKeyboardButton("Show Done", callback_data="show_done")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"Hello {user.first_name}! 👋 Welcome to the Trading Bot!\n\nClick the button below to see our amazing offers.",
            reply_markup=reply_markup
        )
        logger.info("Start message sent successfully")
        
    except Exception as e:
        logger.error(f"Error in start command: {e}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks."""
    try:
        query = update.callback_query
        await query.answer()
        logger.info(f"Button callback received: {query.data}")
        
        if query.data == "show_content":
            # Using a placeholder image - replace with your actual image URL
            image_url = "https://images.unsplash.com/photo-1640340434855-6084b1f4901c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80"
            
            try:
                await query.message.reply_photo(
                    photo=image_url,
                    caption=get_trading_content(),
                    parse_mode='HTML'
                )
                logger.info("Trading content sent with image")
            except Exception as e:
                logger.error(f"Error sending image: {e}")
                # Fallback to text only
                await query.message.reply_text(
                    get_trading_content(),
                    parse_mode='HTML'
                )
        
        elif query.data == "show_done":
            await query.message.reply_text(
                get_done_content(),
                parse_mode='HTML'
            )
            logger.info("Done content sent")
            
    except Exception as e:
        logger.error(f"Error in button callback: {e}")

async def done_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show the done message via command."""
    try:
        await update.message.reply_text(
            get_done_content(),
            parse_mode='HTML'
        )
        logger.info("Done command executed")
    except Exception as e:
        logger.error(f"Error in done command: {e}")

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

def get_done_content():
    return """✅ <b>Done! Congratulations on your new bot.</b>

⚠️ <i>Keep your token secure and store it safely, it can be used by anyone to control your bot.</i>

For a description of the Bot API, see this page: 
https://core.telegram.org/bots/api"""

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f"Exception while handling an update: {context.error}")

def main() -> None:
    """Start the bot."""
    try:
        # Create the Application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Test bot connection
        logger.info("Testing bot connection...")
        
        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("done", done_command))
        application.add_handler(CallbackQueryHandler(button_callback))
        application.add_error_handler(error_handler)
        
        logger.info("Bot starting...")
        print("🤖 Bot is running and waiting for messages...")
        print(f"🤖 Bot token source: {'Environment' if os.getenv('BOT_TOKEN') else 'Code'}")
        
        # Start polling
        application.run_polling(
            poll_interval=1.0,
            timeout=20,
            drop_pending_updates=True
        )
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == '__main__':
    main()
