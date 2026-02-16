from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ====== ВАШИ ДАННЫЕ ======
TOKEN = "8559334940:AAGwmycwxNnY4mpPJXXKHzoqUGJPgyDt0bU"
PDF_LINK = "https://drive.google.com/uc?export=download&id=1a2b3c4d5e6f7g8h9i"  # <- готовая ссылка на PDF
TELEGRAM_CHANNEL_LINK = "https://web.telegram.org/k/#@ai_freelance_startgo"
INSTAGRAM_LINK = "https://www.instagram.com/viktoria.ai.life?igsh=MTliOHJzaWxqOWNsOQ"
YOUTUBE_LINK = "https://www.youtube.com/@фриланс-АИ"
VK_LINK = "https://vk.com/frilans0101"
BOT_LINK = "https://t.me/aware_art_bot?start=welcome"

# ====== Приветственное сообщение ======
WELCOME_TEXT = (
    "Привет! 👋 Я Vika I AI 🤖\n\n"
    "Рада приветствовать тебя! У меня есть для тебя подарок — "
    "PDF с 5 бесплатными нейросетями для фото, видео, текста, голоса и монтажа!\n\n"
    "Выбери, что хочешь сделать:"
)

# ====== Команда /start ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Получить подарок 🎁", callback_data='pdf')],
        [InlineKeyboardButton("Подписаться на канал 🔔", url=TELEGRAM_CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# ====== Обработка нажатий кнопок ======
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "pdf":
        text = (
            "Вот твой PDF с 5 бесплатными нейросетями:\n"
            f"{PDF_LINK}\n\n"
            "Как использовать нейросети:\n"
            "1. Tensor.art — https://tensor.art\n"
            "2. HeyGen — https://www.heygen.com\n"
            "3. ChatGPT — https://chat.openai.com\n"
            "4. ElevenLabs — https://elevenlabs.io\n"
            "5. CapCut — https://www.capcut.com\n\n"
            "Полезные ссылки:\n"
            f"Instagram: {INSTAGRAM_LINK}\n"
            f"YouTube: {YOUTUBE_LINK}\n"
            f"VK: {VK_LINK}\n"
            f"Telegram канал: {TELEGRAM_CHANNEL_LINK}\n"
            "\nСовет: Начни с одной нейросети, потом добавляй остальные!"
        )
        await query.edit_message_text(text=text)

# ====== Запуск бота ======
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Бот Vika I AI запущен...")
    app.run_polling()
