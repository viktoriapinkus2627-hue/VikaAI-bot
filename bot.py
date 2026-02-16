from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# =======================
# ВАШ ТОКЕН
TOKEN = "8559334940:AAGwmycwxNnY4mpPJXXKHzoqUGJPgyDt0bU"

# =======================
# Ссылки на соцсети и канал
INSTAGRAM_LINK = "https://www.instagram.com/viktoria.ai.life?igsh=MTliOHJzaWxqOWNsOQ"
YOUTUBE_LINK = "https://www.youtube.com/@%D1%84%D1%80%D0%B8%D0%BB%D0%B0%D0%BD%D1%81-%D0%90%D0%98"
VK_LINK = "https://vk.com/frilans0101"
TELEGRAM_CHANNEL_LINK = "https://web.telegram.org/k/#@ai_freelance_startgo"

# =======================
# Файл с подарком
PDF_FILE = "gift.png.png"

# =======================
# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 Получить подарок", callback_data='get_gift')],
        [InlineKeyboardButton("📺 Подписаться на канал", url=TELEGRAM_CHANNEL_LINK)],
        [InlineKeyboardButton("Instagram", url=INSTAGRAM_LINK),
         InlineKeyboardButton("YouTube", url=YOUTUBE_LINK),
         InlineKeyboardButton("VK", url=VK_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Я Vika I AI 🤖 — твой помощник по бесплатным нейросетям!\n"
        "У меня есть для тебя подарок: PDF с 5 бесплатными нейросетями для фото, видео, текста, голоса и монтажа.\n\n"
        "Выбери, что хочешь сделать:",
        reply_markup=reply_markup
    )

# =======================
# Обработчик нажатий на кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'get_gift':
        # Отправляем PDF/PNG-файл
        with open(PDF_FILE, "rb") as f:
            await query.message.reply_document(f, filename="5_бесплатных_нейросетей.png")

# =======================
# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Бот Vika I AI запущен...")
    app.run_polling()
