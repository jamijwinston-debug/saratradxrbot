import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from PIL import Image, ImageDraw, ImageFont
import io

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create a welcome image with text
def create_welcome_image():
    # Create a new image with a dark background
    width, height = 800, 400
    image = Image.new('RGB', (width, height), color='#1a1a1a')
    draw = ImageDraw.Draw(image)
    
    try:
        # Try to use a font (this might need adjustment based on your system)
        font_large = ImageFont.truetype("arial.ttf", 36)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        # Fallback to default font
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Add title
    title = "Welcome to Our Trading Community!"
    title_bbox = draw.textbbox((0, 0), title, font=font_large)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    
    draw.text(((width - title_width) / 2, 50), title, fill='#00ff00', font=font_large)
    
    # Add subtitle
    subtitle = "Start Your Journey to Profitable Trading"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    
    draw.text(((width - subtitle_width) / 2, 120), subtitle, fill='#ffffff', font=font_small)
    
    # Add some decorative elements
    draw.rectangle([50, 180, width - 50, 182], fill='#00ff00')
    
    # Convert to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return img_byte_arr

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    
    # Create inline keyboard with a button
    keyboard = [
        [InlineKeyboardButton("🚀 Get Started", callback_data='show_content')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Create and send welcome image
    welcome_image = create_welcome_image()
    
    # Send the image with caption and button
    await update.message.reply_photo(
        photo=welcome_image,
        caption=f"Hi {user.first_name}! 👋\n\nClick the button below to see our amazing offers!",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button clicks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'show_content':
        # Your content with formatting
        content = """🌐 *if You Are A Trader and want To Make Profit Then Welcome To Our Community*! 🔥

We will help You To Recover Your Losses, Just Join our 20$ To 2000$ Compounding Session Daily 💵

🔷 99% Accuracy
🔷 Loss Recovery
🔷 Non Mtg Signals
🔷 Daily 10 to 15 Sureshot Signals
🔷 Expert Trading Signals
🔷 Community Support
🔷 24/7 Assistance

🙋‍♂️ Let's make profitable trades together!

💥 *Join the Winning Team NOW*! 💥
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
            "✅ *Done! Congratulations on your new bot.*",
            parse_mode='Markdown'
        )

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Start the Bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
