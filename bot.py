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

# Bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    
    # Create inline keyboard with a button
    keyboard = [
        [InlineKeyboardButton("🚀 Get Started", callback_data='show_content')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Welcome message with emoji banner (instead of image)
    welcome_message = f"""
✨ {'='*30}
🤖 *WELCOME TO TRADING COMMUNITY* 🚀
✨ {'='*30}

Hi {user.first_name}! 👋

*Ready to start your profitable trading journey?*

Click the button below to discover our exclusive offers! 🔥
    """
    
    # Send the welcome message with button
    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button clicks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'show_content':
        # Your content with formatting
        content = """🌐 *If You Are A Trader And Want To Make Profit Then Welcome To Our Community!* 🔥

We will help You To Recover Your Losses, Just Join our 20$ To 2000$ Compounding Session Daily 💵

✅ *OUR FEATURES:*
🔷 99% Accuracy
🔷 Loss Recovery  
🔷 Non Mtg Signals
🔷 Daily 10 to 15 Sureshot Signals
🔷 Expert Trading Signals
🔷 Community Support
🔷 24/7 Assistance

🙋‍♂️ *Let's make profitable trades together!*

💥 *Join the Winning Team NOW!* 💥
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️

https://t.me/+JBiO5pr6629mOTI1

https://t.me/+JBiO5pr6629mOTI1"""
        
        # Send the content as a new message
        await query.message.reply_text(
            content,
            parse_mode='Markdown',
            disable_web_page_preview=False
        )
        
        # Send the confirmation message
        await query.message.reply_text(
            "✅ *Done! Congratulations on your new bot.* 🎉",
            parse_mode='Markdown'
        )

def main() -> None:
    """Start the bot."""
    # Check if token is available
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN environment variable is not set!")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Start the Bot
    print("✅ Bot is starting...")
    print("🤖 Bot is running and waiting for messages...")
    application.run_polling()

if __name__ == '__main__':
    main()
