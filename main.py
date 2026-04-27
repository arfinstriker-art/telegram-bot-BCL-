import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

BOT_TOKEN = os.getenv("8737522075:AAHjTAOU_k5I_BTKIQJE1qfeYvfY1unXO6k")
OPENAI_API_KEY = os.getenv("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")

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = "You are a funny AI bot 😎"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is alive bro 😎🔥")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ]
    )

    await update.message.reply_text(res.choices[0].message.content)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polliNN
