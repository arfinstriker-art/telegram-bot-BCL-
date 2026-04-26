import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("8737522075:AAHBYriBBOTsmqvxoJJOvQVNwl62cl5gXpY")

CHANNEL = "https://t.me/BCL_Cyber_Legion"
CEO_ID = "@striker_arfin104"

# 😎 Funny replies list
funny_replies = [
    "কি বলসো ভাই 😏🔥",
    "এত সহজ না bro 😎",
    "বুঝি নাই আবার বল 😂",
    "তুই বেশ মজার মানুষ 😆",
    "এইটা আবার কেমন কথা 🤨",
    "হুম... চিন্তা করছি 🤔",
    "এটা dangerous প্রশ্ন 😈🔥",
    "মাথা নষ্ট করিস না bro 🤯😂"
]

# 🔒 Join check
async def is_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

# 🚀 Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_joined(context.bot, update.effective_user.id):
        await update.message.reply_text(f"🚫 আগে channel join করো 😒👇\n{CHANNEL}")
        return

    await update.message.reply_text(
        "😎🔥 BCL AI BOT এ স্বাগতম!\n"
        "👉 কথা বল, মজা কর, প্রশ্ন কর 😏"
    )

# 💬 Message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_joined(context.bot, update.effective_user.id):
        await update.message.reply_text(f"🚫 আগে join করো 😑👇\n{CHANNEL}")
        return

    text = update.message.text.lower()

    # 👑 কে বানাইছে
    if "কে বানাইছে" in text or "who made" in text:
        await update.message.reply_text(
            "😎 আমাকে বানাইছে BANGLADESH CYBER LEGION CEO STRIKER ARFIN 🔥\n"
            f"👑 CEO: {CEO_ID}"
        )

    # 🤖 নাম
    elif "তোমার নাম" in text:
        await update.message.reply_text("😎 আমার নাম BCL AI BOT 🔥")

    # 🚀 টিম
    elif "কোন টিম" in text:
        await update.message.reply_text("🔥 আমি BANGLADESH CYBER LEGION টিমের 😎")

    # 🎯 join
    elif "টিমে ঢুকবো" in text or "join" in text:
        await update.message.reply_text(
            "😏 টিমে ঢুকতে চাইছো নাকি bro?\n"
            f"👉 CEO কে নক দাও: {CEO_ID} 🔥"
        )

    # 😂 random fun reply
    else:
        reply = random.choice(funny_replies)
        await update.message.reply_text(reply)

# ▶️ Run
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()
