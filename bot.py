from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Ваш токен бота
TOKEN = "8559334940:AAGwmycwxNnY4mpPJXXKHzoqUGJPgyDt0bU"

# Ссылки на ваши социальные сети и канал
CHANNEL_LINK = "https://web.telegram.org/k/#@ai_freelance_startgo"
PDF_FILE = "gift.png.png"  # имя файла с PDF/PNG в проекте

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветственное сообщение с кнопками"""
    keyboard = [
        [InlineKeyboardButton("Получить подарок 🎁", callback_data='get_gift')],
        [InlineKeyboardButton("Подписаться на канал 📺", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! 👋\n"
        "Рада тебя видеть! У меня для тебя подарок — PDF с 5 бесплатными нейросетями для фото, видео, текста, голоса и монтажа.\n\n"
        "Выбери одну из кнопок ниже:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()

    if query.data == 'get_gift':
        # Отправляем файл пользователю
        with open(PDF_FILE, "rb") as f:
            await query.message.reply_document(f, filename="5_бесплатных_нейросетей.png")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Команды и кнопки
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Бот запущен...")
    app.run_polling()
