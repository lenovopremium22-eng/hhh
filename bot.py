import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("BOT_TOKEN","7860033244:AAHYhmTrW-CBZxKTI4zRVI_VLfwzTLLXtaY")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 TEST BOT ONLINE!\n\n"
        "✅ Deployment successful\n"
        "🟢 Render Node is working\n\n"
        "Commands:\n"
        "/ping - Check bot\n"
        "/id - Show your Telegram ID"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 PONG!\n\n🟢 Bot is working perfectly.")


async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 Your Telegram ID:\n`{update.effective_user.id}`",
        parse_mode="Markdown",
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("id", user_id))

    print("🤖 Test bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
