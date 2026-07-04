import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Hello! Welcome to Michael Music Bot.\n\nUse /play followed by a song name.\n\nExample:\n/play Shape of You"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ Please enter a song name.\nExample:\n/play Shape of You"
        )
        return

    song = " ".join(context.args)

    await update.message.reply_text(
        f"🔍 Searching for: {song}\n\n🎵 Music playback will be added in the next step."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
