import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from keep_alive import keep_alive


TOKEN = os.getenv("BOT_TOKEN")


# وقتی کاربر /start میزند
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🕵️‍♂️ به Elite Society خوش آمدید

شما وارد یک پرونده محرمانه شده‌اید.

آماده باشید...
اولین ماموریت شما به زودی آغاز می‌شود.

🎯 برای دریافت ماموریت‌ها منتظر بمانید.
        """
    )


# خطای نبودن توکن
if not TOKEN:
    print("ERROR: BOT_TOKEN not found!")


def main():

    # فعال کردن وب سرور برای UptimeRobot
    keep_alive()


    # ساخت ربات
    app = Application.builder().token(TOKEN).build()


    # دستور start
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    print("Elite Society Bot Started!")


    # اجرای دائمی ربات
    app.run_polling()



if __name__ == "__main__":
    main()
